with open("day-8.input.txt") as f:
	map = f.read().strip().split("\n")

	# Find all antennas, as well as by frequency
	all_antennas = []
	antennas = {}
	for idx,row in enumerate(map):
		for rowidx,char in enumerate(row):
			if char == '.':
				continue
			if char not in antennas:
				antennas[char] = []

			antennas[char].append((rowidx, idx))
			all_antennas.append((rowidx, idx))

# Find all antinodes
antinodes = []
antinodes_harmonics = []
for frequency in antennas:
	ant = antennas[frequency]
	for idx_a in range(len(ant)):
		for idx_b in range(len(ant)):
			if idx_a == idx_b:
				continue
			# Find antinodes for antennas (idx_a) and (idx_b)
			antenna_a = ant[idx_a]
			antenna_b = ant[idx_b]

			rise = antenna_b[1] - antenna_a[1]
			run = antenna_b[0] - antenna_a[0]

#			antinodes.append((-run + antenna_a[0], -rise + antenna_a[1]))
#			antinodes.append((run + antenna_b[0], rise + antenna_b[1]))

			# Calculate any additional harmonics
			def harmonic(number):
				positions = [
					(-(run*number) + antenna_a[0], -(rise*number) + antenna_a[1]),
					((run*number) + antenna_b[0], (rise*number) + antenna_b[1])
				]
				for idx,i in enumerate(positions):
					if i[0] < 0 or i[1] < 0:
						# Outside left or top bounds
						positions[idx] = False
					if i[0] >= len(map[0]) or i[1] >= len(map):
						# Outside right or bottom bounds
						positions[idx] = False

				return positions

			# Increase harmonic level until we leave both bounds
			antinodes += harmonic(1)

			harmon = 1
			while True:
				result = harmonic(harmon)
				harmon += 1
				# If both are out of bounds, we're done
				if result == [False, False]:
					break
				# Otherwise, add any in-bounds values
				antinodes_harmonics += [i for i in result if i != False]

def validate_antinodes(inp):
	# Remove all duplicates or off-map antinodes
	valid_antinodes = []
	for i in inp:
		if i in valid_antinodes:
			continue
		if i == False:
			# Failed bounds check above
			continue

#		if i[0] < 0 or i[1] < 0:
#			continue
#		if i[0] >= len(map[0]) or i[1] >= len(map):
#			continue

		valid_antinodes.append(i)

	return valid_antinodes

# Add all anteannas to harmonics list
antinodes_harmonics += all_antennas

antinodes = validate_antinodes(antinodes)
antinodes_harmonics = validate_antinodes(antinodes_harmonics)

# Modified from day 6
def visualize(antinodes):
	for y in range(len(map)):
		for x in range(len(map[y])):
			char = map[y][x]
			if (x, y) in antinodes:
				if char == '.': char = '#'
				char = '\033[31m' + char + '\033[39m'
			print(char, end='')
		print() # Next line


visualize(antinodes)
print("Part 1:",len(antinodes))

print("\n")

visualize(antinodes_harmonics)
print("Part 2:",len(antinodes_harmonics))
