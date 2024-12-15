import input

plots = [[i for i in j] for j in input.split("\n")]
print(plots)

def find_neighbors(point):
	""" Finds all neighbors with the same letter """
	# Extract position X and Y
	x, y = point

	# Get start value and target next value
	value = plots[y][x]

	# Look on each (avialable) side for the target value
	results = []
	if y > 0 and plots[y-1][x] == value:
		results.append([x, y-1])
	if y < len(plots)-1 and plots[y+1][x] == value:
		results.append([x, y+1])
	if x > 0 and plots[y][x-1] == value:
		results.append([x-1, y])
	if x < len(plots[0])-1 and plots[y][x+1] == value:
		results.append([x+1, y])

	return results

# Directions:
#   1
# 2 + 3
#   4
def grow_in_direction(points, point, direction):
	""" Expands from point in direction (using the provided list of valid points) until no more matching points are found """

	# Clone list so we don't modify it
	point = [i for i in point]

	# Make all elements tuples
	points = tuple(tuple(i) for i in points)

	found = []
	while True:
		if direction == 1:
			point[1] -= 1
		elif direction == 2:
			point[0] -= 1
		elif direction == 3:
			point[0] += 1
		elif direction == 4:
			point[1] += 1

		if tuple(point) not in points:
			return found

		found.append(tuple(point))

region_prices = []
def grow_region(point, existing_points=None):
	""" Finds all plots with same letter connected to the point """
	points = [point]

	neighbors = find_neighbors(point)
	for i in neighbors:
		# Ignore any existing spaces we've already found
		if i in points or (existing_points and i in existing_points):
			continue
		# Add to list of valid spaces
		points.append(i)
		# Recurse and ignore duplicates
		region_grown = grow_region(i, points + (existing_points or []))
		points += [j for j in region_grown if j not in points]

	if existing_points==None:
		#print(points)
		# Find number of neighbors
		num_neigh = 0
# Sides:
#   1
# 2 + 3
#   4
		sides = {1:[], 2:[], 3:[], 4:[]}
		for i in points:
			if [i[0]+1, i[1]] in points:
				num_neigh += 1
			else:
				sides[3].append(i)

			if [i[0]-1, i[1]] in points:
				num_neigh += 1
			else:
				sides[2].append(i)

			if [i[0], i[1]+1] in points:
				num_neigh += 1
			else:
				sides[4].append(i)

			if [i[0], i[1]-1] in points:
				num_neigh += 1
			else:
				sides[1].append(i)


		total_sides = 0
		for side_type in sides:
			found_sides = []
			for point in sides[side_type]:
				#print(point,found_sides,sep='\t')

				if tuple(point) in found_sides:
					continue

				found_sides.append(tuple(point))
				total_sides += 1

				# Grow side and add all other points to list

				if side_type in [1,4]:
					# Grow horizontally
					found_sides += grow_in_direction(sides[side_type], tuple(point), 2)
					found_sides += grow_in_direction(sides[side_type], tuple(point), 3)
				else:
					# Grow vertically
					found_sides += grow_in_direction(sides[side_type], tuple(point), 1)
					found_sides += grow_in_direction(sides[side_type], tuple(point), 4)

		area = len(points)
		peri = (4*area)-(num_neigh)
		price_a = area * peri
		price_b = area * total_sides

#		print("Nei:",num_neigh)
#		print("Area:",area)
#		print("Peri:",(4*area)-(num_neigh))
#		print("Price:",price)

		letter = plots[point[1]][point[0]]
		region_prices.append((letter, price_a, price_b))

	return points

found_points = []
for x in range(len(plots[0])):
	for y in range(len(plots)):
		if [x, y] in found_points:
			continue
		found_points += grow_region([x, y])

print("Part 1:",sum(i[1] for i in region_prices))
print("Part 2:",sum(i[2] for i in region_prices))
