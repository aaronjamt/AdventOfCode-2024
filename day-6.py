import time
with open("day-6.input.txt") as f:
	map=f.read().strip().split("\n")

	# Find all obstacles and the guard
	obstacles = []
	for idx,row in enumerate(map):
		for rowidx,char in enumerate(row):
			if char == '#':
				obstacles.append((rowidx, idx))

			elif char == '^':
				guard_position = (rowidx, idx)
				guard_direction = 0
			elif char == '<':
				guard_position = (rowidx, idx)
				guard_direction = 1
			elif char == '>':
				guard_position = (rowidx, idx)
				guard_direction = 2
			elif char == 'v':
				guard_position = (rowidx, idx)
				guard_direction = 3

# Directions:
#   0
# 3 + 1
#   2

# Returns None if the guard has left or a tuple of its new position and direction
def move_guard(current_position, direction, obstacles):
	new_position = list(current_position)
	if direction == 0:
		new_position[1] -= 1
	elif direction == 1:
		new_position[0] += 1
	elif direction == 2:
		new_position[1] += 1
	elif direction == 3:
		new_position[0] -= 1
	else:
		raise ValueError("Invalid direction:"+repr(direction))
	new_position = tuple(new_position)

	# Check if outside map
	if new_position[0] < 0 or new_position[1] < 0 or new_position[0] > len(map[0]) or new_position[1] > len(map):
		return None

	if new_position in obstacles:
		# Cannot move that direction! Turn right 90 degrees and try again
		direction = (direction + 1) % 4
		new_position = current_position

	return new_position, direction

def visualize(guard_position, travelled_position, travelled_direction):
	# Clear screen
	print('\033[2J\033[1;1H')
	for y in range(len(map)):
		for x in range(len(map[y])):
			char = map[y][x]
			if guard_position == (x, y):
				char = 'G'
			elif (x, y) in travelled_position:
				idx = travelled_position.index((x, y))
				direction = travelled_direction[idx]

				if direction == 0:
					char = '^'
				elif direction == 1:
					char = '>'
				elif direction == 2:
					char = 'v'
				elif direction == 3:
					char = '<'
				else:
					char = "*"
			print(char, end='')
		print() # Next line
	time.sleep(0.02)

def simulate(guard_position, guard_direction, obstacles):
	travelled_position = []
	travelled_direction = []
	while True:
		result = move_guard(guard_position, guard_direction, obstacles)
		if result is None:
			break

		# If we're in a new position, add to the list
		if guard_position not in travelled_position:
			travelled_position.append(guard_position)
			travelled_direction.append(guard_direction)
		# We're somewhere we've been before
		else:
			# If we're also facing the same way, we're in a loop
			if travelled_direction[travelled_position.index(guard_position)] == guard_direction:
				return False

		guard_position, guard_direction = result

#		visualize(guard_position, travelled_position, travelled_direction)

	return travelled_position, travelled_direction

travelled_position, travelled_direction = simulate(guard_position, guard_direction, obstacles)
print("Part 1:",len(travelled_position))

def is_blocking_obstacle(obstacle):
	new_obstacles = obstacles + [obstacle,]
	if simulate(guard_position, guard_direction, new_obstacles) == False:
		return obstacle
	else:
		return None


#blocking_obstacles = []


#for y in range(len(map)):
#	for x in range(len(map[0])):
#		if is_blocking_obstacle((x,y)):
#			blocking_obstacles.append((x,y))

from concurrent.futures import ProcessPoolExecutor
with ProcessPoolExecutor() as executor:
  all_positions = [(x, y) for x in range(len(map[0])) for y in range(len(map))]
  results = executor.map(is_blocking_obstacle, all_positions)
  print("Processing part 2...")
  found = 0
  done = 0
  total = len(all_positions)
  for result in results:
    done += 1
    print(f" {all_positions[done-1]}:\t{done}/{total}:\t{done/total*100}%        ", end="\r")
    if result != None:
      print(result, " "*64)
      found += 1

print("\nPart 2:",found)
