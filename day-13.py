import input

machines = []
for i in input.split("\n\n"):
	machines.append([[int(k[2:]) for k in j.split(': ')[1].split(', ')] for j in i.split('\n')])

# Calculates the cost of pressing the buttons a certain number of times
cost_of_presses = lambda a,b: (a*3)+b
# Calculate how far we move given a number of button presses
distance_moved = lambda a,b,a_amt,b_amt: tuple([(a[0]*a_amt+b[0]*b_amt),(a[1]*a_amt+b[1]*b_amt)])
distance_moved = lambda a,b,a_amt,b_amt: tuple([(a[0]*a_amt+b[0]*b_amt),(a[1]*a_amt+b[1]*b_amt)])

def determine_optimal_movement(machine):
	""" Determines how many times to push A button vs B button to reach the target """

	a_dist, b_dist, target = machine

	# Yay for math
	a_amt = (b_dist[0]*target[1] - target[0]*b_dist[1]) / (a_dist[1]*b_dist[0] - a_dist[0]*b_dist[1])
	b_amt = (a_dist[0]*target[1] - target[0]*a_dist[1]) / (a_dist[0]*b_dist[1] - a_dist[1]*b_dist[0])

	# If not a whole number, it's not solvable
	if int(a_amt) != a_amt or int(b_amt) != b_amt:
		return None

	a_amt = int(a_amt)
	b_amt = int(b_amt)

	return (a_amt, b_amt)

	"""
	# Move A max times first
	a_amt = min((target[0] // a_dist[0]), (target[1] // a_dist[1]))
	b_amt = 0

	solution = None
	while True:
		# Calculate total distance moved
		move_x, move_y = distance_moved(a_dist, b_dist, a_amt, b_amt)
		if move_x == target[0] and move_y == target[1]:
			# We found a solution!
			price = cost_of_presses(a_amt, b_amt)
			if solution is None or price < solution[0]:
				solution = (price, move_x, move_y)
			# Decrease A movement to continue searching
			a_amt -= 1
		elif move_x > target[0] or move_y > target[1]:
			# If we've overshot, decrease A movement
			a_amt -= 1

			# Increase B movement while it's <= the amount we just moved back by
			while move_x < target[0] and move_y < target[1]:
				b_amt += 1
				move_x += b_dist[0]
				move_y += b_dist[1]

			b_amt -= 1
		else:
			# If we're not far enough, increase B movement
			b_amt += 1


		#print(f"  {a_amt}\t{b_amt}")

		# If the A movement is negative, we're done
		if a_amt < 0:
			break

	return solution

from concurrent.futures import ProcessPoolExecutor
def process_multithreaded(machines):
	result_sum = 0

	with ProcessPoolExecutor() as executor:
		results = executor.map(determine_optimal_movement, machines)
		print("Processing...")
		done = 0
		total = len(machines)
		for result in results:
			done += 1
			print(f" {done}/{total}:\t{done/total*100}%        ", end="\r")
			if result != None:
				print(result, " "*64)
				result_sum += result[0]

	return result_sum

print("Part 1:",process_multithreaded(machines))

# Add 10000000000000 to each price coord
for i in machines:
	i[2][0] += 10000000000000
	i[2][1] += 10000000000000

print("Part 2:",process_multithreaded(machines))

"""

def find_total_cost(machines):
	total_cost = 0
	for machine in machines:
		# Figure out how many times to press each button
		presses = determine_optimal_movement(machine)

		# If None, we can't move there
		if presses is None:
#			print("Unable to move to") #,prize)
			continue

#		print("Can move!")
		cost = cost_of_presses(presses[0], presses[1])

#		print(f"It costs {cost} to press A {presses[0]} and B {presses[1]} times!")
		total_cost += cost
	return total_cost

print("Part 1:",find_total_cost(machines))

# Add 10000000000000 to each price coord
for i in machines:
	i[2][0] += 10000000000000
	i[2][1] += 10000000000000

print("Part 2:",find_total_cost(machines))
