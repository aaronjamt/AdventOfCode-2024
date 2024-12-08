import os.path, sys, inspect

# Find the name of the file that was initially called
filename = inspect.stack()[-1].filename

# Extract just its filename, without the path to it
filename = os.path.basename(filename)

# Extract the day number
try:
	day_number = int(filename.replace("day-", "").replace(".py", ""))
except ValueError:
	# If not possible, instead prompt the user for that information
	while True:
		try:
			day_number = int(input("Please enter the day number: "))
			break
		except ValueError:
			print("Invalid input, try again.")

# Check command line arguments to select file to load
input_type = 'input'
if len(sys.argv) > 1:
	if sys.argv[1].lower().startswith('e'):
		# Use example file, rather than main input file
		input_type = 'example'

with open(f"day-{day_number}.{input_type}.txt") as f:
	input = f.read().strip()

# `input` now contains the input for the program, replace this module with its value
sys.modules[__name__] = input
