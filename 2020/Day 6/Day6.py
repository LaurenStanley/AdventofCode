#Please Update Accordingly
data_file = 'Input.txt'
current_section = 2

#Loads data from text file.
#This function will split out data by line and
#return as a list of floats
def get_data():
	with open(data_file, 'r') as file:
		data = file.read().split('\n')
	new_data = []
	group = []
	for point in data:
		if point != '':
			group.append(point)
		if point == '':
			new_data.append(group)
			group = []
	new_data.append(group)
	return new_data

def parse_groups(groups):
	yeses = 0
	for group in groups:
		letters = []
		for person in group:
			for question in person:
				if question not in letters:
					letters.append(question)
		seperate_yeses = len(letters)
		yeses += seperate_yeses
	return yeses

def parse_groups2(groups):
	yeses = 0
	for group in groups:
		groupies = len(group)
		letter_list = []
		for person in group:
			for letters in person:
				letter_list.append(letters)
		letter_list.sort()
		new_list = []
		for let in letter_list:
			if let not in new_list:
				new_list.append(let)
		for x in new_list:
			count = letter_list.count(x)
			if count == groupies:
				yeses += 1
	return yeses

#Runs part two of the puzzle
def part_two(data):
	yeses = parse_groups2(data)
	print(yeses)


#Runs part one of the puzzle
def part_one(data):
	yeses = parse_groups(data)
	print(yeses)

def main():
	data = get_data()
	#print(data)
	if current_section == 1:
		part_one(data)
	elif current_section == 2:
		part_two(data)

if __name__ =="__main__":
	main()