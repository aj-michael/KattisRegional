import sys


def foo(m, n, t):
    return 'AC' if n**t < m else 'TLE'

if __name__ == '__main__':
    data = sys.stdin.readlines()[0].strip().split()
    m = int(data[0])
    n = int(data[1])
    t = int(data[2])
    print foo(m,n,t)
