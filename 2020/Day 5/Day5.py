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

def parse_ticket(data):
	seat_ids = []
	for ticket in data:
		ticket = ticket[0]
		row = get_row(ticket[:7])
		column = get_column(ticket[7:])
		seat_id = get_seat_id(row,column)
		seat_ids.append(seat_id)
	#print(seat_ids)
	if current_section == 1:
		return(max(seat_ids))
	if current_section == 2:
		return(seat_ids)

def get_row(row_info):
	decimal = 0 
	binary = list(str(row_info)) #convert binary to a list 
	binary = binary[::-1]      #reverse the list 
	power = 0   #declare power variable (for 1st elem == 0) 
	for number in binary: 
		if number == 'B': 
			decimal += 2**power     
		power += 1 #increase power by 1    
	return(decimal)

def get_column(row_info):
	decimal = 0 
	binary = list(str(row_info)) #convert binary to a list 
	binary = binary[::-1]      #reverse the list 
	power = 0   #declare power variable (for 1st elem == 0) 
	for number in binary: 
		if number == 'R': 
			decimal += 2**power     
		power += 1 #increase power by 1    
	return(decimal)

def get_seat_id(row,column):
	seat_id = row*8 + column
	return(seat_id)

def integer_seat_ids(seat_ids):
	new_ids = []
	for x in seat_ids:
		x = int(x)
		new_ids.append(x)
	new_ids.sort()
	return new_ids

def find_my_seat(seat_ids):
	seat_ids = integer_seat_ids(seat_ids)
	print(seat_ids)
	max_real_seat = int(max(seat_ids))
	min_real_seat = int(min(seat_ids))
	valid_seats = list(range(min_real_seat,max_real_seat+1))
	for seat in seat_ids:
		valid_seats.remove(seat)
	print(valid_seats)
	return valid_seats
	
#Runs part two of the puzzle
def part_two(data):
	seat_ids = parse_ticket(data)
	my_seat = find_my_seat(seat_ids)
	print('My seat is', my_seat)
	return(my_seat)
#Runs part one of the puzzle
def part_one(data):
	max_id = parse_ticket(data)
	print('The maximum seat ID is', max_id)
	return(max_id)

def main():
	data = get_data()
	#print(data)
	if current_section == 1:
		solution = part_one(data)
	elif current_section == 2:
		solution = part_two(data)
	

if __name__ =="__main__":
	main()