with open("day-5.input.txt") as f:
	x=f.read().strip().split("\n")

	# Split into rules and updates sections, and split each section's lines with their delimiters
	rules = [i.split('|') for i in x[:x.index('')]]
	updates = [i.split(',') for i in x[x.index('')+1:]]

	# Make all values ints
	rules = [[int(j) for j in i] for i in rules]
	updates = [[int(j) for j in i] for i in updates]

def is_valid(update):
	for rule in rules:
		if rule[0] in update and rule[1] in update:
			# If the first part of the rule is later, the update is invalid
			if update.index(rule[0]) > update.index(rule[1]):
				return False

	# If all checks pass
	return True

# Swaps two items in a list
def swap(lst, idx1, idx2):
	orig1 = lst[idx1]
	orig2 = lst[idx2]

	lst[idx1] = orig1
	lst[idx2] = orig2
	return lst

def fix(update):
	item_order = []
	for i in update:
		new_idx = len(item_order)
		for rule in rules:
			if i not in rule:
				continue

			left = rule[0]
			right = rule[1]

			if i == left:
				# Needs to be left of some other item
				if right in item_order:
					new_idx = min(new_idx, item_order.index(right))
			elif i == right:
				# Needs to be right of some other item
				if left in item_order:
					new_idx = max(new_idx, item_order.index(left)+1)
		item_order.insert(new_idx, i)

	return item_order

total_part_1 = 0
total_part_2 = 0
for i in updates:
	print(is_valid(i),i)

	if is_valid(i):
		middle_number = i[len(i) // 2]
		total_part_1 += middle_number
	else:
		i = fix(i)

		middle_number = i[len(i) // 2]
		total_part_2 += middle_number


print("Part 1:",total_part_1)
print("Part 2:",total_part_2)
