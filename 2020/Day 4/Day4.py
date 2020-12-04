#Please Update Accordingly
data_file = 'InputTest1.txt'
current_section = 2

#Loads data from text file.
#This function write each passport as a dictionary
def get_data():
	f = open(data_file, 'r')
	lines = f.read()
	f.close()
	lines = lines.split('\n')
	data_list = []
	current_id_dict = {}
	for i in range(len(lines)):
		line = lines[i]
		items = line.split(' ')
		#print(items)
		for item in items:
			item = item.split(':')
			#print(item)
			if len(item) <= 1:
				data_list.append(current_id_dict)
				current_id_dict = {}
			else:
				current_id_dict[item[0]] = item[1]
	data_list.append(current_id_dict)
	return data_list

#Determines whether each passport has all of the appropriate fields
def determine_validity(data):
	valid_passports = 0
	#necessary_fields = ['ecl','pid','eyr','hcl','byr','iyr','cid','hgt']
	for passport in data:
		remaining_fields = ['ecl','pid','eyr','hcl','byr','iyr','cid','hgt']
		keys = passport.keys()
		for key in keys:
			remaining_fields.remove(key)
		if len(remaining_fields) == 0 or remaining_fields == ['cid']:
			if current_section == 1:
				valid_passports += 1
			if current_section == 2:
				is_valid = determine_info_validity(passport)
				if is_valid == True:
					valid_passports += 1
	return valid_passports

#Feeds the valid passport through the conditions for each field.
def determine_info_validity(passport):
	is_valid = True
	#Birth Year Condition
	if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
		is_valid = False
		return is_valid
	#Issue Year Condition
	if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
		is_valid = False
		return is_valid
	#Expiration Year Condition
	if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
		is_valid = False
		return is_valid
	#Height Condition
	if determine_valid_height(passport['hgt']) == False:
		is_valid = False
		return is_valid
	#Hair Color Condition
	if determine_valid_hair(passport['hcl']) == False:
		is_valid = False
		return is_valid
	#Eye Color Condition
	if determine_valid_eye(passport['ecl']) == False:
		is_valid = False
		return is_valid
	#Password ID Condition
	if determine_valid_pid(passport['pid']) == False:
		is_valid = False
		return is_valid
	return is_valid

#Determines height field validity by reading units and height value. Throws out readings with non-integers in the value position
def determine_valid_height(height):
	valid_height = False
	units = height[-2:]
	try:
		value = int(height[:-2])
	except ValueError:
		return valid_height
	if units == 'cm':
		if 150 <= value <= 193:
			valid_height = True
	if units == 'in':
		if 59 <= value <= 76:
			valid_height = True
	return valid_height

#Reads the hair color codes
def determine_valid_hair(hair):
	is_valid = True
	valid_characters = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
	if hair[0] != '#':
		is_valid = False
	hair_code = hair[1:]
	for character in hair_code:
		if character not in valid_characters:
			is_valid = False
	return is_valid

#Reads the eye codes
def determine_valid_eye(eye):
	is_valid = True
	valid_characters = ['amb','blu','brn','gry','grn','hzl','oth']
	if eye not in valid_characters:
		is_valid = False
	return is_valid

#Reads the passport code
def determine_valid_pid(pid):
	is_valid = True
	valid_characters = ['0','1','2','3','4','5','6','7','8','9']
	if len(pid) != 9:
		is_valid = False
	for character in pid:
		if character not in valid_characters:
			is_valid = False
	return is_valid
#Runs part two of the puzzle
def part_two(data):
	valid_passports = determine_validity(data)
	return valid_passports

#Runs part one of the puzzle
def part_one(data):
	valid_passports = determine_validity(data)
	return valid_passports

def main():
	data = get_data()
	if current_section == 1:
		solution = part_one(data)
	elif current_section == 2:
		solution = part_two(data)
	print('There are', solution,'valid passports')

if __name__ =="__main__":
	main()