
def import_file_content():
  with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

  return lines

# DAY 1
import re
lines = import_file_content()
print(lines)

# Part 1
final_sum = 0
for line in lines:
  line_numbers = re.findall(r'\d', line)
  line_sum = line_numbers[0] + line_numbers[-1]
  final_sum += int(line_sum)

print('=============')
print('Part 1')
print(final_sum)
print('=============')

# Part 2
spelled_out_numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
final_sum = 0
for line in lines:
  line_numbers = []
  for i, letter in enumerate(line):
    if letter.isdigit():
      line_numbers.append(letter)
    else:
      for z, word in enumerate(spelled_out_numbers):
        if line.startswith(word, i):
          line_numbers.append(str(z))
  line_sum = line_numbers[0] + line_numbers[-1]
  final_sum += int(line_sum)


print('=============')
print('Part 2')
print(final_sum)
print('=============')