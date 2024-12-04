with open("day-2.input.txt", "r") as f:
	x = [i for i in f.read().strip().split("\n") if i]

def is_safe(items):
#		print("=======")
#		print(items)
		is_safe = True

		prev = items[0]
		if items[1] == items[0]:
			print("Unsafe because no direction")
			return False
		direction = items[1] > items[0]
		for i in items[1:]:
			moved = i - prev
#			if moved == 0:
#				print("Unsafe because number stayed the same!")
#				is_safe = False
#				break
			if (moved > 0) != direction:
				print("Unsafe because direction changed!")
				is_safe = False
				break
			if moved < 0:
				moved = -moved
			if moved < 1:
				print("Unsafe because too small change!")
				is_safe = False
				break
			if moved > 3:
				print("Unsafe because too large change!")
				is_safe = False
				break

			prev = i

		return is_safe

safe = 0
safe_with_problem_damper = 0
print(len(x))
for line in x:
	items = [int(i) for i in line.split(' ')]
	if is_safe(items):
		print("Safe!")
		safe += 1
	else:
		for item in range(len(line)):
			others = [j for i, j in enumerate(items) if i != item]
			if is_safe(others):
				print("Safe by removing:",item)
				safe_with_problem_damper += 1
				break

print("Total safe:",safe)
print("Total safe with problem damper:",safe + safe_with_problem_damper)
