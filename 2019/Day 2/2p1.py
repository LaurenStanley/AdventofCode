data_file = 'GravityAssist.txt'

def parse_data():
    f = open(data_file, 'r')
    data = f.read()
    f.close()
    strings = data.split(',')
    integers = []
    for i in strings:
        i = int(i)
        integers.append(i)
    return integers

def restore_data(integers,verb,noun):
    integers[1] = noun
    integers[2] = verb
    return integers

def interpreter(integers):
    i = 0
    while True:
        opcode = integers[i]
        if opcode == 1:
            integers = opcode1(integers,i)
        if opcode == 2:
            integers = opcode2(integers,i)
        if opcode == 99:
            return integers
            break
        i = i +4

def opcode1(integers,i):
    input1 = integers[integers[i+1]]
    input2 = integers[integers[i+2]]
    output = input1+input2
    integers[integers[i+3]] = output
    return integers

def opcode2(integers,i):
    input1 = integers[integers[i+1]]
    input2 = integers[integers[i+2]]
    output = input1*input2
    integers[integers[i+3]] = output
    return integers 

def find_VN():
    for v in range(100):
        for n in range(100):
            integers = parse_data()
            new_integers = restore_data(integers, v, n)
            new_list = interpreter(new_integers)
            if new_list[0] == 19690720:
                value = 100*n + v
                return value
    print("VN Not Found")

def main():
    code = find_VN()
    print(code)
    
if __name__ == "__main__" :
    main()
    
