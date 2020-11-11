data_file = 'Input.txt'

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
    j = 0
    while True:
        opcode = get_code(integers[i])
        parameters = get_parameters(integers[i])
        #print(integers)
        #print(integers[i])
        #print(i)
        if opcode == 1:
          integers = opcode1(integers,i,parameters)
          j = 4
        if opcode == 2:
          integers = opcode2(integers,i,parameters)
          j = 4
        if opcode == 3:
          integers = opcode3(integers,i)
          j = 2
        if opcode == 4:
          integers = opcode4(integers,i,parameters)
          j = 2
        if opcode == 5:
          integers,o, m = opcode5(integers,i,parameters)
          if m == True:
            i = int(o)
            j = 0
          else:
            j = 3
        if opcode == 6:
          integers, o, m = opcode6(integers,i,parameters)
          if m == True:
            i = int(o)
            j = 0
          else:
            j = 3
        if opcode == 7:
          integers = opcode7(integers,i,parameters)
          j = 4
        if opcode == 8:
          integers = opcode8(integers,i,parameters)
          j = 4
        if opcode == 99:
            return integers
            break
        i += j

def get_code(integer):
  integer = str(integer)
  opcode = int(integer[-2:])
  return opcode

def get_parameters(integer):
  integer = str(integer)
  parameters = []
  for i in range(3):
    try:
      indexValue = 3 + i
      parameter = int(integer[-indexValue])
      parameters.append(parameter)
    except IndexError:
      parameter = int(0)
      parameters.append(parameter)
  return(parameters)

def opcode1(integers,i,p):
  if p[0] == 0:
    input1 = integers[integers[i+1]]
  if p[0] == 1:
    input1 = integers[i+1]
  if p[1] == 0:
    input2 = integers[integers[i+2]]
  if p[1] == 1:
    input2 = integers[i+2]
  output = input1+input2
  integers[integers[i+3]] = output
  return integers

def opcode2(integers,i,p):
  if p[0] == 0:
    input1 = integers[integers[i+1]]
  if p[0] == 1:
    input1 = integers[i+1]
  if p[1] == 0:
    input2 = integers[integers[i+2]]
  if p[1] == 1:
    input2 = integers[i+2]
  output = input1*input2
  integers[integers[i+3]] = output
  return integers

def opcode3(integers,i): 
  input1 = int(input('Code3 Requires Input: '))
  integers[integers[i+1]] = input1
  return integers

def opcode4(integers,i,p):
  if p[0] == 0:
    output = integers[integers[i+1]]
  if p[0] == 1:
    output = integers[i+1]
  print('Code4 Output: ',output)
  return integers

def opcode5(integers,i,p):
  modifiedBool = False
  output = 0
  #print(p)
  if p[0] == 0:
    input1 = integers[integers[i+1]]
  if p[0] == 1:
    input1 = integers[i+1]
  if input1 != 0:
    if p[1] == 0:
      output = integers[integers[i+2]]
    if p[1] ==1:
      output = integers[i+2]
    modifiedBool = True 
  #print(output)
  return integers, output, modifiedBool

def opcode6(integers,i,p):
  modifiedBool = False
  output = 0
  if p[0] == 0:
    input1 = integers[integers[i+1]]
  if p[0] == 1:
    input1 = integers[i+1]
  if input1 == 0:
    if p[1] == 0:
      output = integers[integers[i+2]]
    if p[1] ==1:
      output = integers[i+2]
    modifiedBool = True 
  #print(output)
  return integers, output, modifiedBool

def opcode7(integers,i,p):
  if p[0] == 0:
    input1 = integers[integers[i+1]]
  if p[0] == 1:
    input1 = integers[i+1]
  if p[1] == 0:
    input2 = integers[integers[i+2]]
  if p[1] == 1:
    input2 = integers[i+2]
  if input1 < input2:
    integers[integers[i+3]] = 1
  else:
    integers[integers[i+3]] = 0
  return integers

def opcode8(integers,i,p):
  if p[0] == 0:
    input1 = integers[integers[i+1]]
  if p[0] == 1:
    input1 = integers[i+1]
  if p[1] == 0:
    input2 = integers[integers[i+2]]
  if p[1] == 1:
    input2 = integers[i+2]
  if input1 == input2:
    integers[integers[i+3]] = 1
  else:
    integers[integers[i+3]] = 0
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
    inputs = parse_data()
    interpreter(inputs)
    
if __name__ == "__main__" :
    main()
    
