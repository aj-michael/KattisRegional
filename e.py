import sys

data = [x.strip() for x in sys.stdin.readlines()][:-1]

# All inputs are strings.
def solve(x, s, p, c):
  simap = dict((s[i],i) for i in xrange(0,len(s)))
  pimap = dict((p[i],i) for i in xrange(0,len(p)))
  def S(index):
    return s[index]
  def Si(chara):
    return simap[chara]
  def P(index):
    return p[index]
  def Pi(chara):
    return pimap[chara]
  n = len(c)
  d = int(n**1.5+x)%n
  mmap = {}
  j = d
  mmap[j] = P(Si(c[j]))
  while len(mmap) < n:
    mmap[(j-1)%n] = P(Si(mmap[j]) ^ Si(c[(j-1)%n]))
    j = (j-1)%n
  return ''.join(mmap[i] for i in xrange(0,n))


if __name__ == '__main__':
  i = 0
  solutions = []
  while i < len(data):
    x = int(data[i])
    s = data[i+1]
    p = data[i+2]
    c = data[i+3]
    solutions += [solve(x, s, p, c)]
    i += 4
  print '\n'.join(solutions)
