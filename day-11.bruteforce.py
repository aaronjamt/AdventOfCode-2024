import input, time

stones = [int(i) for i in input.split(" ")]

def blink(stones):
	new_stones = []

	for i in stones:
		if i == 0:
			new_stones.append(1)
		elif len(str(i)) % 2 == 0:
			j = str(i)
			middle = len(j) // 2
			new_stones += [int(j[:middle]), int(j[middle:])]
		else:
			new_stones += [i * 2024]

	return new_stones

# Blink 25 times
for i in range(25):
	print("Blink:",i)
	stones = blink(stones)

print("Part 1:",len(stones))

# Blink 50 more times
for i in range(0,50):
	print("Blink:",i+25,len(stones))

	stones = blink(stones)

print("Part 2:",len(stones))
