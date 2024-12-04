DEBUG = False

with open("day-4.input.txt", "r") as f:
	input = f.read().strip().split("\n")
#	input_rotated = [''.join([input[i][j] for i in range(len(input[0]))]) for j in range(len(input))]

#	print(input)

# 0 1 2
# 3   4
# 5 6 7
def move_in_dir(row, col, dir):
	if dir == 0:
		if row == 0 or col == 0:
			return False
		return (row-1, col-1)
	elif dir == 1:
		if row == 0:
			return False
		return (row-1, col)
	elif dir == 2:
		if row == 0 or col + 1 == len(input[0]):
			return False
		return (row-1, col+1)

	elif dir == 3:
		if col == 0:
			return False
		return (row, col-1)
	elif dir == 4:
		if col + 1 == len(input[0]):
			return False
		return (row, col+1)

	elif dir == 5:
		if row + 1 == len(input) or col == 0:
			return False
		return (row+1, col-1)
	elif dir == 6:
		if row + 1 == len(input):
			return False
		return (row+1, col)
	elif dir == 7:
		if row + 1 >= len(input) or col + 1 >= len(input[0]):
			return False
		return (row+1, col+1)
	return False

def test(row, col, string, dir):
	idxes = []
	for idx in range(len(string)):
		letter = string[idx]
		if input[row][col] != letter:
			return False
		idxes.append([col,row])
		# Check if we can continue moving, but only if not the last letter
		if idx < len(string) - 1:
			result = move_in_dir(row, col, dir)
			if result == False:
				return False
			row, col = result
	return idxes

#print('T',test(9, 3, 'XMAS', 0))
#exit()

x_indexes = [[k for k,v in enumerate(row) if v == 'X'] for row in input]

uncovered = []
total = 0
for row,row_val in enumerate(x_indexes):
	for col in row_val:
		# (row, col) is the location of an "X"
#		print(row,col)
		for i in range(8):
			result = test(row, col, 'XMAS', i)
			if result != False:
#				print("Found at", row, col, i)
				total += 1
				uncovered += result
print("Part 1:",total)

if DEBUG:
	for y,y_val in enumerate(input):
		for x,x_val in enumerate(y_val):
			if [x,y] in uncovered:
				print(input[y][x], end='')
			else:
				print('.', end='')
		print()
#======================

uncovered = []

a_indexes = [[k for k,v in enumerate(row) if v == 'A'] for row in input]

total_mas = 0
for row,row_val in enumerate(a_indexes):
	for col in row_val:
		# (row, col) is the location of an "A"

		# Check all diagonals
		diags = [[move_in_dir(row, col, i), i] for i in [0, 2, 7, 5]]
		diags = [[i[0][0], i[0][1], i[1]] if i[0] != False else False for i in diags]

		valid_diags = []
		for diag in diags:
			if diag == False:
				valid_diags.append(False)
				continue
			drow, dcol, oppdir = diag
			# Find opposite direction
			if oppdir == 0: dir = 7
			elif oppdir == 2: dir = 5
			elif oppdir == 5: dir = 2
			elif oppdir == 7: dir = 0
			else: continue

			result = test(drow, dcol, 'MAS', dir)
			valid_diags.append(result)

		valid_diags = [i for i in valid_diags if i is not False]
		"""
		if (valid_diags[0] != False and valid_diags[1] != False):
			uncovered += valid_diags[0] + valid_diags[1]
			valid = True
		if (valid_diags[2] != False and valid_diags[3] != False):
			uncovered += valid_diags[2] + valid_diags[3]
			valid = True
"""
		if len(valid_diags) == 2:
			total_mas += 1
			for i in valid_diags:
				uncovered += i

print("Part 2:",total_mas) # Each pair of MAS is only counted once

if DEBUG:
	for y,y_val in enumerate(input):
		for x,x_val in enumerate(y_val):
			if [x,y] in uncovered:
				print(input[y][x], end='')
			else:
				print('.', end='')
		print()
#======================
"""
def search_string(table, target):
	found = 0
	for row in table:
		idx = 0
		try:
			while True:
				row = row[row.index(target) + 1:]
				found += 1
#				print(f"Found @ {idx}: {found}")
		except ValueError:
			continue

	return found
def search(target):
	return (
		search_string(input, target) + search_string(input, target[::-1]) +
		search_string(input_rotated, target) + search_string(input_rotated, target[::-1])
	)

print(search("XMAS"))
"""
