import input, time

layout = []

# Convert numbers in the file (alternating occupied/free blocks) into a list of file IDs and '.'s (for free space)
occupied = True
file_id = 0
for i in input:
	i = int(i)
	if occupied:
		for j in range(i):
			layout.append(file_id)
		file_id += 1
	else:
		for j in range(i):
			layout.append('.')

	occupied = not occupied

blocks = []
free = 0

def swap(lst, idx_a, idx_b):
	""" Swaps 2 elements in a list (or string) by index """
	is_str = False
	if type(lst) == str:
		is_str = True
		lst = [i for i in lst]

	item_a = lst[idx_a]
	item_b = lst[idx_b]

	lst[idx_a] = item_b
	lst[idx_b] = item_a

	if is_str:
		return ''.join(lst)

	return lst

def is_contiguous(layout):
	""" Determines whether all file data is contiguous """
	first_free = layout.index('.')
	# Check if any non-period (AKA non-free) blocks exist after that point
	remainder = layout[first_free:]
	occupied_blocks = [i != '.' for i in remainder]
	# If any blocks are occupied, it's not contiguous
	if True in occupied_blocks:
		return False
	return True

def checksum(layout):
	""" Calculate checksum by adding up the result of multiplying each blocks' position with the file ID number it contains """
	if type(layout) != list:
		layout = [i for i in layout]

	result = 0
	for idx,val in enumerate(layout):
		if val == '.':
			continue
		result += idx * val

	return result

def part_one(layout):
	""" Solves part one """
	# Convert into boolean for search
	occupied_blocks = [i != '.' for i in layout]

	total = len(layout)
	begin = 0
	end = total
	while True:
		mini_range = occupied_blocks[begin:end]

		first_free = mini_range.index(False)
		last_occupied = mini_range[::-1].index(True) + 1

		new_begin = first_free
		new_end = total - last_occupied

		first_free = begin + first_free
		last_occupied = end - last_occupied

		begin = new_begin
		end = new_end

		#print(f" First free: {first_free}\t\tLast occupied: {last_occupied}")

		swap(layout, first_free, last_occupied)
		swap(occupied_blocks, first_free, last_occupied)

		if first_free == last_occupied - 1:
			break
	return layout

def find_free_space_of_size(layout, length):
	""" Searches for a block of contiguous free space of at least length blocks """
	potential_block_start = None
	for i in range(len(layout)):
		if potential_block_start == None and layout[i] == '.':
			potential_block_start = i
		elif potential_block_start != None and layout[i] != '.':
			if i - potential_block_start >= length:
				return potential_block_start
			else:
				potential_block_start = None
	return None

def part_two(layout):
	""" Solves part two """
	# Find max file ID (plus one because we decrement before comparing)
	file_id = max([i for i in layout if i != '.']) + 1

	# Convert into boolean for search
	occupied_blocks = [i != '.' for i in layout]

	while True:
		#print(' '.join([str(i) for i in layout]))

		# Looks like someone didn't read the instructions properly...

#		# Find last file on disk
#		last_occupied = None
#		for i in range(len(layout), 0, -1):
#			if layout[i-1] != '.':
#				last_occupied = i-1
#				break
#		if last_occupied == None:
#			raise ValueError("Unable to find last occupied block! Is the drive empty?")

		# Countdown so I know it's not stuck and can make a mental estimate of how long it'll take
		print(f" {file_id} left...    \r", end="")

		# Find file start by ID
		file_id -= 1
		if file_id < 0:
			break
		file_start = layout.index(file_id)

		# Find length of that file
		file_end = file_start
		while True:
			file_end += 1
			if file_end >= len(layout) or layout[file_end] != file_id:
				file_end -= 1
				break

		# file_start and last_occupied are the range of the file
		file_length = file_end - file_start + 1

		# Now find free space that'll fit the file
		free_space = find_free_space_of_size(layout, file_length)
		if free_space == None:
			continue
			#raise Exception(f"Not enough free space for file of size {file_length}!")

		# Don't move the file later in the disk
		if free_space > file_start:
			continue

		# Move the file into the free space
		for i in range(file_length):
			layout[free_space + i] = layout[file_start + i]
			layout[file_start + i] = '.' # Now free

	return layout

## Clone the list before passing so it doesn't get modified
#part_one_layout = part_one([i for i in layout])
#print("Part 1:",checksum(part_one_layout))

# Clone the list before passing so it doesn't get modified
part_two_layout = part_two([i for i in layout])
print("Part 2:",checksum(part_two_layout))
