def interpreter(integers,input_values,i,iii):
    j = 0
    while True:
        opcode = get_code(integers[i])
        parameters = get_parameters(integers[i])
        #print(opcode)
        #print(integers)
        if opcode == 1:
          integers = opcode1(integers,i,parameters)
          j = 4
        if opcode == 2:
          integers = opcode2(integers,i,parameters)
          j = 4
        if opcode == 3:
          integers = opcode3(integers,i,input_values[iii])
          iii += 1
          j = 2
        if opcode == 4:
          integers,output = opcode4(integers,i,parameters)
          return(output,integers, i+2, iii)
          #print(output)
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
            return None, None, None, None
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

def opcode3(integers,i,input_value): 
  input1 = input_value
  integers[integers[i+1]] = input1
  return integers

def opcode4(integers,i,p):
  if p[0] == 0:
    output = integers[integers[i+1]]
  if p[0] == 1:
    output = integers[i+1]
  return integers, output

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
