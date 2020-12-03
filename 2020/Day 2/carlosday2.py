f = open('Input.txt', 'r')
lines = f.readlines()

valid_count = 0
#part 1
for line in lines:
    data = line.split()
    min_number = data[0].split('-')[0]
    max_number = data[0].split('-')[1]
    special_char = data[1].split(':')[0]
    instance_count = 0
    for letter in data[2]:
        if letter == special_char:
            instance_count += 1
    if int(min_number) <= instance_count <= int(max_number):
        valid_count += 1
print(valid_count)        
#part 2
second_count = 0
for line in lines:
    data = line.split()
    first_position = data[0].split('-')[0]
    second_position = data[0].split('-')[1]
    special_char = data[1].split(':')[0]
    cond_1 = False
    cond_2 = False
    if len(data[2]) >= int(first_position):
        if data[2][int(first_position)-1] == special_char:
            cond_1 = True
    if len(data[2]) >= int(second_position):
        if data[2][int(second_position)-1] == special_char:
            cond_2 = True
    if cond_1 != cond_2:
        second_count += 1
print(second_count)        