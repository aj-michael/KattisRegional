import sys
def spaces(x):
  return len(x.split(' ')) - 1
data = [x.strip() for x in sys.stdin.readlines()]
data = filter(lambda x: x != '-1 -1', data)
i = 0
solutions = []
while i < len(data):
  max_width = int(data[i])
  i += 1
  total_height = 0
  largest_width = 0
  current_width = 0
  current_height = 0
  while i < len(data) and spaces(data[i]) == 1:
    rwidth, rheight = [int(x) for x in data[i].split(' ')]
    if (current_width + rwidth > max_width):
      largest_width = max(largest_width, current_width)
      total_height += current_height
      current_width = 0
      current_height = 0
    else:
      current_height = max(current_height, rheight)
      current_width += rwidth
      i += 1
  largest_width = max(largest_width, current_width)
  total_height += current_height
  solutions += [str(largest_width) + ' x ' + str(total_height)]
print '\n'.join(solutions[:-1])
