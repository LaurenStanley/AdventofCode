def interpreter(integers):
    j = 0
    i = 0
    relative_base = 0
    while True:
        #print('Current Integer',integers[i],'\ni value', i, '\nrelative base value', relative_base,'\n')
        opcode = get_code(integers[i])
        parameters = get_parameters(integers[i])
        #print(opcode)
        #print(parameters)
        #print(integers[0:30])
        if opcode == 1:
          #print('Current Integer',integers[i],'\ni value', i, '\nrelative base value', relative_base,'\n')
          integers = opcode1(integers,i,parameters, relative_base)
          j = 4
        if opcode == 2:
          integers = opcode2(integers,i,parameters, relative_base)
          j = 4
        if opcode == 3:
          integers = opcode3(integers,i,parameters, relative_base)
          j = 2
        if opcode == 4:
          integers,output = opcode4(integers,i,parameters, relative_base)
          #return(output)
          #print(output)
          j = 2
        if opcode == 5:
          integers,o, m = opcode5(integers,i,parameters, relative_base)
          if m == True:
            i = int(o)
            j = 0
          else:
            j = 3
        if opcode == 6:
          integers, o, m = opcode6(integers,i,parameters, relative_base)
          if m == True:
            i = int(o)
            j = 0
          else:
            j = 3
        if opcode == 7:
          integers = opcode7(integers,i,parameters, relative_base)
          j = 4
        if opcode == 8:
          integers = opcode8(integers,i,parameters, relative_base)
          j = 4
        if opcode == 9:
          integers, relative_base = opcode9(integers,i,parameters,relative_base)
          j = 2
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

def opcode1(integers,i,p,relative_base):
  if p[0] == 0:
    input1 = integers[integers[i+1]]
  if p[0] == 1:
    input1 = integers[i+1]
  if p[0] == 2:
    input1 = integers[integers[i+1]+relative_base]
  if p[1] == 0:
    input2 = integers[integers[i+2]]
  if p[1] == 1:
    input2 = integers[i+2]
  if p[1] == 2:
    input2 = integers[integers[i+2]+relative_base]
  output = input1+input2
  if p[2] == 0:
    integers[integers[i+3]] = output
  if p[2] == 2:
    integers[integers[i+3]+relative_base] = output
  return integers

def opcode2(integers,i,p,relative_base):
  if p[0] == 0:
    input1 = integers[integers[i+1]]
  if p[0] == 1:
    input1 = integers[i+1]
  if p[0] == 2:
    input1 = integers[integers[i+1]+relative_base]
  if p[1] == 0:
    input2 = integers[integers[i+2]]
  if p[1] == 1:
    input2 = integers[i+2]
  if p[1] == 2:
    input2 = integers[integers[i+2]+relative_base]
  output = input1*input2
  if p[2] == 0:
    integers[integers[i+3]] = output
  if p[2] == 2:
    integers[integers[i+3]+relative_base] = output
  return integers

def opcode3(integers,i,p,relative_base): 
  input1 = input('Input: ')
  input1 = int(input1)
  #print(integers[i],integers[i+1],i)
  if p[0] == 0:
    integers[integers[i+1]] = input1
  if p[0] == 2:
    integers[integers[i+1]+relative_base] = input1
  return integers

def opcode4(integers,i,p,relative_base):
  if p[0] == 0:
    output = integers[integers[i+1]]
  if p[0] == 1:
    output = integers[i+1]
  if p[0] == 2:
    output = integers[integers[i+1]+relative_base]
  print(output)
  return integers,output

def opcode5(integers,i,p,relative_base):
  modifiedBool = False
  output = 0
  #print(p)
  if p[0] == 0:
    input1 = integers[integers[i+1]]
  if p[0] == 1:
    input1 = integers[i+1]
  if p[0] == 2:
    input1 = integers[integers[i+1]+relative_base]
  if input1 != 0:
    if p[1] == 0:
      output = integers[integers[i+2]]
    if p[1] ==1:
      output = integers[i+2]
    if p[1] == 2:
      output = integers[integers[i+2]+relative_base]
    modifiedBool = True 
  #print(output)
  return integers, output, modifiedBool

def opcode6(integers,i,p,relative_base):
  modifiedBool = False
  output = 0
  if p[0] == 0:
    input1 = integers[integers[i+1]]
  if p[0] == 1:
    input1 = integers[i+1]
  if p[0] == 2:
    input1 = integers[integers[i+1]+relative_base]
  if input1 == 0:
    if p[1] == 0:
      output = integers[integers[i+2]]
    if p[1] ==1:
      output = integers[i+2]
    if p[1] == 2:
      output = integers[integers[i+2]+relative_base]
    modifiedBool = True 
  #print(output)
  return integers, output, modifiedBool

def opcode7(integers,i,p,relative_base):
  if p[0] == 0:
    input1 = integers[integers[i+1]]
  if p[0] == 1:
    input1 = integers[i+1]
  if p[0] == 2:
    input1 = integers[integers[i+1]+relative_base]
  if p[1] == 0:
    input2 = integers[integers[i+2]]
  if p[1] == 1:
    input2 = integers[i+2]
  if p[1] == 2:
    input2 = integers[integers[i+2]+relative_base]
  if input1 < input2:
    if p[2] == 0:
      integers[integers[i+3]] = 1
    if p[2] == 2:
      integers[integers[i+3]+relative_base] = 1
  else:
    if p[2] == 0:
      integers[integers[i+3]] = 0
    if p[2] == 2:
      integers[integers[i+3]+relative_base] = 0
  return integers

def opcode8(integers,i,p,relative_base):
  if p[0] == 0:
    input1 = integers[integers[i+1]]
  if p[0] == 1:
    input1 = integers[i+1]
  if p[0] == 2:
    input1 = integers[integers[i+1]+relative_base]
  if p[1] == 0:
    input2 = integers[integers[i+2]]
  if p[1] == 1:
    input2 = integers[i+2]
  if p[1] == 2:
    input2 = integers[integers[i+2]+relative_base]
  if input1 == input2:
    if p[2] == 0:
        integers[integers[i+3]] = 1
    if p[2] == 2:
      integers[integers[i+3]+relative_base] = 1
  else:
    if p[2] == 0:
      integers[integers[i+3]] = 0
    if p[2] == 2:
      integers[integers[i+3]+relative_base] = 0
  return integers

def opcode9(integers,i,p,relative_base):
  if p[0] == 0:
    input1 = integers[integers[i+1]]
  if p[0] == 1:
    input1 = integers[i+1]
  if p[0] == 2:
    input1 = integers[integers[i+1]+relative_base]
  relative_base = relative_base + input1
  return integers, relative_base
