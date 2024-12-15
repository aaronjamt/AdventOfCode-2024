import input
from functools import cache

stones = [int(i) for i in input.split(" ")]

@cache
def stones_after_blinks(stone, times):
	""" Blinks at a single stone {times} times """
	# If we're done, return that there's only a single stone here
	if times == 0:
		return 1

	# If the stone is zero, it becomes one
	if stone == 0:
		return stones_after_blinks(1, times-1)

	# If it's an even-length string, split in half
	if len(str(stone)) % 2 == 0:
		# Find the center of the string
		stone_str = str(stone)
		middle = len(stone_str) // 2

		# Calculate left side
		left = int(stone_str[:middle])
		left = stones_after_blinks(left, times-1)

		# Calculate right side
		right = int(stone_str[middle:])
		right = stones_after_blinks(left, times-1)

		# Return total
		return left+right

	# Otherwise, the stone is multipled by 2024
	return stones_after_blinks(stone*2024, times-1)

def blink(stones, times):
	""" Blinks at a list of stones {times} times and returns the total number of stones at the end """
	return sum([stones_after_blinks(stone, times) for stone in stones])

print("Part 1:",blink(stones, 25))
print("Part 2:",blink(stones, 75))
