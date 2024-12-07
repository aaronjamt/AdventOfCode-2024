with open("day-7.input.txt") as f:
	inp = f.read().strip().split("\n")

	# Split into a list of (result, (numbers, ))
	equations = []
	for line in inp:
		line = line.split(":")
		result = int(line[0])
		numbers = line[1].strip().split(" ")
		numbers = [int(i) for i in numbers]

		equations.append((result, tuple(numbers)))

def int_to_operators(value, minimum_length=0):
	# Convert to binary, then to string of '*' and '+'
	value = bin(value)[2:]
	if len(value) < minimum_length:
		value = ('0' * (minimum_length-len(value))) + value
	value = value.replace('0', '*')
	value = value.replace('1', '+')
	return value

def int_to_operators_trinary(value, minimum_length=0):
	# Convert to trinary, then to string of '*', '+', and '|'
	result = ''
	while value > 0:
		digit = value % 3
		result = ['*','+','|'][digit] + result
		value = value // 3

	if len(result) < minimum_length:
		result = ('*' * (minimum_length-len(result))) + result

	return result

def try_equation(equation, operators):
	target_result = equation[0]
	numbers = equation[1]

	if type(operators) == int:
		operators = int_to_operators(operators, len(numbers) - 1)

	result = numbers[0]
	numbers = numbers[1:]
	for i in range(len(numbers)):
		if operators[i] == '*':
			result *= numbers[i]
		elif operators[i] == '+':
			result += numbers[i]
		elif operators[i] == '|':
			# Concatenate
			result = int(str(result) + str(numbers[i]))
	return result == target_result

def try_equation_part_two(equation, operators):
	numbers = equation[1]
	if type(operators) == int:
		operators = int_to_operators_trinary(operators, len(numbers) - 1)

	return try_equation(equation, operators)

part_one_sum = 0
part_two_sum = 0
for equation in equations:
	equation_len = len(equation[1])
	num_operators = equation_len - 1
	part_one_success = False
	for i in range(2**num_operators):
		if try_equation(equation, i):
			part_one_sum += equation[0]
			part_one_success = True
			break
	if not part_one_success:
		# Only try adding part 2's operator if part 1 failed
		for i in range(3**num_operators):
			if try_equation_part_two(equation, i):
				part_two_sum += equation[0]
				break

print("Part 1:",part_one_sum)
print("Part 2:",part_one_sum+part_two_sum)
