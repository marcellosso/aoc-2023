import re
from functools import reduce

def import_file_content():
  with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

  return lines

lines = import_file_content()
print(lines)
# 12 red cubes, 13 green cubes, and 14 blue cubes

limits = {
    'red': 12,
    'green': 13,
    'blue': 14
}

# PART 1
final_sum = 0
for i, line in enumerate(lines):
  formatted = re.sub(r'Game \d+: ', ' ', line)
  games = formatted.split(';')
  is_possible = True
  for game in games:
    cubes = re.findall(r'\b(\d+) *(blue|red|green+)', game)
    for cube in cubes:
      if int(cube[0]) > limits[cube[1]]:
        is_possible = False
  if is_possible:
    final_sum = final_sum + i + 1

print('=============')
print('Part 1')
print(final_sum)
print('=============')

# PART 2
final_sum = 0
for i, line in enumerate(lines):
  formatted = re.sub(r'Game \d+: ', ' ', line)
  games = formatted.split(';')
  colors_val_dict = {
      'red': 0,
      'blue': 0,
      'green': 0
  }
  
  for game in games:
    cubes = re.findall(r'\b(\d+) *(blue|red|green+)', game)
    for cube in cubes:
      colors_val_dict[cube[1]] = max(colors_val_dict[cube[1]], int(cube[0]))
  
  mult_res = reduce(lambda x, value: x * value, colors_val_dict.values())
  final_sum = final_sum + mult_res


print('=============')
print('Part 2')
print(final_sum)
print('=============')