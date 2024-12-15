import input
input = input.split('\n')

# Convert all to ints
input = [[int(j) for j in i] for i in input]

trailheads = []
for rowidx,row in enumerate(input):
	for colidx,col in enumerate(row):
		if col == 0:
			trailheads.append((colidx, rowidx))

def search_for_increasing(start_position):
	""" Searches for neighbor tiles that are exactly one larger than the current """
	# Extract position X and Y
	x, y = start_position

	# Get start value and target next value
	start_value = input[y][x]
	next_value = start_value + 1

	# Look on each (available) side for the target value
	options = []
	if y > 0 and input[y-1][x] == next_value:
		options.append([x, y-1])
	if y < len(input)-1 and input[y+1][x] == next_value:
		options.append([x, y+1])
	if x > 0 and input[y][x-1] == next_value:
		options.append([x-1, y])
	if x < len(input[0])-1 and input[y][x+1] == next_value:
		options.append([x+1, y])

	return options

def follow_trails_from(start_position):
	""" Recursively follows a trail starting from some position, only visiting tiles that have the current value + 1 """
	# If the current value is 9, return that we found one valid trail here
	if input[start_position[1]][start_position[0]] == 9:
		return [[start_position]]

#	print("Searching from:",start_position)

	valid_trails = []
	positions = search_for_increasing(start_position)
#	print("Found:",positions)
	for next_position in positions:
		for trail in follow_trails_from(next_position):
#			print("Trail:",trail)
			valid_trails.append([start_position,] + trail)
#		valid_trails += follow_trails_from(next_position)

#	print("Total valid:",valid_trails)
	return valid_trails

scores = []
ratings = []
for start in trailheads:
	trails = follow_trails_from(start)
	# Store number of unique trails to raitings list
	ratings.append(len(trails))

	# Filter out duplicate endings
	unique_trails = []
	trail_ends = []
	for trail in trails:
		if trail[-1] in trail_ends:
			continue
		unique_trails.append(trail)
		trail_ends.append(trail[-1])

	# Score is number of unique trail endings we can find
	score = len(unique_trails)

	scores.append(score)
	print("Trail score:",score)

print("Part 1:",sum(scores))
print("Part 2:",sum(ratings))
