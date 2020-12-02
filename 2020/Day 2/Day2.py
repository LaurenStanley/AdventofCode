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

def parse_passwords(passwords_and_parameters):
	parsed_passwords = []
	for info in passwords_and_parameters:
		info = str(info[0])
		x = info.split("-")
		minimum = int(x[0])
		y = x[1].split(' ',1)
		maximum = int(y[0])
		z = y[1].split(': ')
		letter = z[0]
		password = z[1] 
		pw_info = [minimum,maximum,letter,password]
		parsed_passwords.append(pw_info)
	return(parsed_passwords)

def determine_validity(parsed_passwords):
	number_of_valid_passwords = 0
	for info in parsed_passwords:
		#print(info)
		number_of_matches = 0
		for character in info[3]:
			if character == info[2]:
				number_of_matches += 1
		if number_of_matches >= info[0] and number_of_matches<= info[1]:
			number_of_valid_passwords += 1
	return(number_of_valid_passwords)

def determine_validity2(parsed_passwords):
	number_of_valid_passwords = 0
	for info in parsed_passwords:
		first_location = info[0]-1
		second_location = info[1]-1
		password = info[3]
		if password[first_location] == info[2]:
			if password[second_location] != info[2]:
				number_of_valid_passwords += 1
		elif password[second_location] == info[2]:
			if password[first_location] != info[2]:
				number_of_valid_passwords += 1
	return(number_of_valid_passwords)


#Runs part two of the puzzle
def part_two(data):
	parsed = parse_passwords(data)
	number_valid = determine_validity2(parsed)
	return(number_valid)
#Runs part one of the puzzle
def part_one(data):
	#print(data)
	parsed = parse_passwords(data)
	number_valid = determine_validity(parsed)
	return(number_valid)

def main():
	data = get_data()
	if current_section == 1:
		solution = part_one(data)
	elif current_section == 2:
		solution = part_two(data)
	print('The solution is',solution)

if __name__ =="__main__":
	main()