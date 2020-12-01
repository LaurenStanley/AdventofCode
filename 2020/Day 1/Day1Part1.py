#Please Update Accordingly
data_file = 'Input.txt'
current_section = 2

#Loads data from text file.
#This function will split out data by line and
#return as a list of floats
def get_data():
    f = open(data_file, 'r')
    lines = f.readlines()
    f.close()
    data_list = []
    for line in lines:
        line = line.splitlines()
        line = float(line[0])
        data_list.append(line)
    return data_list

#Finds two values which add up to 2020
def find_two_values(expenses):
	values = []
	expenses1 = expenses
	for expense1 in expenses1:
		#print(expense1)
		expenses1.remove(expense1)
		expenses2 = expenses1
		for expense2 in expenses2:
			if expense1+expense2 == 2020:
				values.append(expense1)
				values.append(expense2)
	return(values)

#Finds three values which add up to 2020
def find_three_values(expenses):
	values = []
	for expense1 in expenses:
		for expense2 in expenses:
			for expense3 in expenses:
				if expense1+expense2+expense3 == 2020:
					working_set = [expense1,expense2,expense3]
					values.append(working_set)
	return(values[0])

#Multiplies the values as specificied by the prompt
def multiply_values(values):
	product = 1
	for value in values:
		product = product*value
	return(product)


#Runs part two of the puzzle
def part_two():
	expenses = get_data()
	values = find_three_values(expenses)
	solution = multiply_values(values)
	print('The solution is ',solution)

#Runs part one of the puzzle
def part_one():
	expenses = get_data()
	values = find_two_values(expenses)
	solution = multiply_values(values)
	print('The solution is ',solution)

def main():
	if current_section == 1:
		part_one()
	elif current_section == 2:
		part_two()

if __name__ =="__main__":
	main()