list_a = []
list_b = []

with open("day-1.input.txt", "r") as f:
	x = f.read()
	x = [[j for j in i.split(' ') if j] for i in x.split("\n")]

for i in x:
	if len(i) == 2:
		list_a.append(int(i[0]))
		list_b.append(int(i[1]))

list_a = sorted(list_a)
list_b = sorted(list_b)

total = 0
for i in range(len(list_a)):
	diff = list_b[i] - list_a[i]
	if diff < 0: diff = -diff

#	print(list_a[i], list_b[i], diff, sep='\t')

	total += diff

print("Part 1:", total)


# ------------------------------------


total = 0
for i in range(len(list_a)):
	item = list_a[i]
	occurances = len([j for j in list_b if j == item])
	similarity = item * occurances

	total += similarity

print("Part 2:",total)
