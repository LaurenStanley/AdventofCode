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
        data_list.append(line)
    return data_list

def ride_tobaggen(map,x_move,y_move):
	current_x = 0
	current_y = 0
	tree_count = 0
	total_rows = len(map)
	still_in_map = True
	while still_in_map is True:
		current_row = map[current_y]
		current_row = current_row[0]
		current_location = current_row[current_x]
		if current_location == '#':
			tree_count += 1
		current_y += y_move
		current_x += x_move
		if current_x > len(current_row)-1:
			current_x = current_x-len(current_row)
		if current_y > len(map)-1:
			still_in_map = False
	return tree_count
	
def try_multiple_slopes(data):
	product = 1
	slope_combos = [[1,1],[3,1],[5,1],[7,1],[1,2]]
	for slope in slope_combos:
		multiplier = ride_tobaggen(data,slope[0],slope[1])
		print(multiplier)
		product = product*multiplier
	return(product)


#Runs part two of the puzzle
def part_two(data):
	product = try_multiple_slopes(data)
	print('The solution is:',product)
	
#Runs part one of the puzzle
def part_one(data):
	tree_count = ride_tobaggen(data,3,1)
	print('The solution is:',tree_count)

def main():
	data = get_data()
	#print(data)
	if current_section == 1:
		part_one(data)
	elif current_section == 2:
		part_two(data)

if __name__ =="__main__":
	main()