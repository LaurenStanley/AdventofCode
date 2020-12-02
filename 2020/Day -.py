#Please Update Accordingly
data_file = 'InputTest1.txt'
current_section = 1

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
        data_list.append(line)
    return data_list

#Runs part two of the puzzle
def part_two(data):
	print(2)
#Runs part one of the puzzle
def part_one(data):
	print(1)

def main():
	data = get_data()
	print(data)
	if current_section == 1:
		part_one(data)
	elif current_section == 2:
		part_two(data)

if __name__ =="__main__":
	main()