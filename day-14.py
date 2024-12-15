import input, re
input = input.split("\n")

robots = []
for line in input:
	matches = re.findall(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
	if len(matches) < 1:
		print("No match:",line)
		continue
	if len(matches) > 1:
		print(f"Warning: too many matches found for robot: '{line}'")
	match = matches[0]
	px, py, vx, vy = [int(i) for i in match]

	robots.append(((px, py), (vx, vy)))

def position_after(map_size, position, velocity, seconds):
	""" Calculates where the robot will be, given a starting position and velocity, the size of the map, and a number of seconds """
	# Add velocity*seconds
	position = [position[0] + (velocity[0]*seconds), position[1] + (velocity[1]*seconds)]
	# Wrap arond screen edges
	position = [position[0] % map_size[0], position[1] % map_size[1]]
	# Convert back to tuple
	return tuple(position)

def robots_in_quadrants(map_size, robots):
	""" Determine how many robots are in each quadrant """
	middle = [i//2 for i in map_size]
	gutter = [i%2==1 for i in map_size]

	result = [0, 0, 0, 0]

	left_right = None
	top_bottom = None

	for i in robots:
		x,y = i
		if gutter[0] and x == middle[0]:
			continue
		if gutter[1] and y == middle[1]:
			continue

		if x < middle[0]:
			left_right = 0
		else:
			left_right = 1

		if y < middle[1]:
			top_bottom = 0
		else:
			top_bottom = 1

		# If it's in the middle, continue
		if left_right is None or top_bottom is None:
			continue

		result[(top_bottom*2) + left_right] += 1
	return result

map_size = (101, 103) # Given in problem
duration = 100 # seconds

# Calculate robots in each quadrant
robots_after = [position_after(map_size, i[0], i[1], duration) for i in robots]

quadrants = robots_in_quadrants(map_size, robots_after)
print(quadrants)
safety_factor = 1
for i in quadrants:
	safety_factor *= i
print("Part 1 (12):",safety_factor)

# ------ Part Two ------

import time, os, threading

# Let user see part one result
print("Continuing to part two in 5 seconds...")
time.sleep(5)

def visualize(robots_after):
	""" Visualize the robots in the map """
	result = []
	for y in range(map_size[1]):
		line = []
		for x in range(map_size[0]):
			num = len([i for i in robots_after if i == (x,y)])
			if num == 0:
				num = '.'

			line.append(str(num)+' ')
		result.append(''.join(line))
	return '\n'.join(result)

for sec in range(1000000):
	# Column = 23 (for me), find by switching if statements below
	robots_after = [position_after(map_size, i[0], i[1], sec) for i in robots]
	num_in_col = [i for i in robots_after if i[0] == 23]
	num_in_col = len(num_in_col)

	#if True:
	if num_in_col == 33: # Find by counting
		# Clear screen and draw visual, as well as number of seconds, then give the user a chance to see and react
		print('\033[2J\033[H' + visualize(robots_after))
		print()
		print(sec)

		time.sleep(0.25)
