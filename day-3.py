with open("day-3.input.txt", "r") as f:
	input = f.read().strip()

import re
regex = re.compile(r"(?:mul\((\d+,\d+)\))|(do(?:n't)?\(\))")
#instructions = [[int(j) for j in i.split(',')] for i in regex.findall(input)]
instructions = regex.findall(input)

total_a = 0
total_b = 0
b_state = True
for instruction in instructions:
	if len(instruction[0]) > 0:
		value = instruction[0].split(',')
		value = int(value[0]) * int(value[1])
		total_a += value
		if b_state: total_b += value
	elif len(instruction[1]) > 0:
		if instruction[1] == 'do()':
			b_state = True
		elif instruction[1] == "don't()":
			b_state = False


print("Part 1:",total_a)
print("Part 2:",total_b)
