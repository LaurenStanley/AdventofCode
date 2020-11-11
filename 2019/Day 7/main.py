data_file = 'InputTest4.txt'
import IntComputer
from itertools import permutations

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

def possible_phase_sequences(phase_values):
  sequence_list = list(permutations(phase_values))
  return(sequence_list)

def try_all_possible_sequences(sequence_list):
  value_list = []
  value_dict = {}
  for sequence in sequence_list:
    print(sequence)
    value = run_amplifiers(sequence,0)
    value_list.append(value)
    value_dict[value] = sequence
  print(value_list)
  maximum_value = max(value_list)
  best_sequence = value_dict[maximum_value]
  return(best_sequence, maximum_value)

def run_amplifiers(sequence,input_value):
  inputs = parse_data()
  outputA,codeA = IntComputer.interpreter(inputs,[0,sequence[0]])
  outputB,codeB = IntComputer.interpreter(inputs,[outputA,sequence[1]])
  outputC,codeC = IntComputer.interpreter(inputs,[outputB,sequence[2]])
  outputD,codeD = IntComputer.interpreter(inputs,[outputC,sequence[3]])
  outputE,codeE = IntComputer.interpreter(inputs,[outputD,sequence[4]])
  print(outputE,codeE)
  while True:
    outputA,codeA = IntComputer.interpreter(inputs,[outputE,outputE])
    if codeA == 99:
      outputA = outputE
    outputB,codeB = IntComputer.interpreter(inputs,[outputA,outputA])
    if codeB == 99:
      outputB = outputB
    outputC,codeC = IntComputer.interpreter(inputs,[outputB,outputB])
    if codeC == 99:
      outputC = outputB
    outputD,codeD = IntComputer.interpreter(inputs,[outputC,outputC])
    if outputD == 99:
      outputD = outputC
    outputE,codeE = IntComputer.interpreter(inputs,[outputD,outputD])
    if codeE == 99:
      return outputE
            
    #if codeA == 99:
      outputA = outputE

#          if outputD == None:
#            outputD = outputC
#        if outputC == None:
#          outputC = outputB
#       if outputB == None:
#        outputB = outputA
#    if outputA == None:
#      outputA = outputE
#    print(outputE)
    if outputA == None and outputB == None and outputC == None and outputD == None:
      print('Halted')
      return outputE
      break

def interpreter(integers,input_values):
    i = 0
    j = 0
    iii = 1
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
          iii = 0
          j = 2
        if opcode == 4:
          integers,output = opcode4(integers,i,parameters)
          return output
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
            return None
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


def get_section():
  while True:
    part = input('Part One or Part Two: ').upper()
    if part == '1' or part == 'ONE':
      return 1
    elif part == '2' or part == 'TWO':
      return 2
    else:
      print('Invalid Input')
      continue

def part_two():
  sequence_list = possible_phase_sequences([5,6,7,8,9])
  best_sequence, thruster_value = try_all_possible_sequences(sequence_list)
  print('The highest value sequence is: ', best_sequence)
  print('The output thruster value is: ',thruster_value)

def part_one():
  #inputs = parse_data()
  sequence_list = possible_phase_sequences([0,1,2,3,4])
  best_sequence, thruster_value = try_all_possible_sequences(sequence_list)
  print('The highest value sequence is: ', best_sequence)
  print('The output thruster value is: ',thruster_value)

def main():
  get_part = get_section()
  if get_part == 1:
    part_one()
  elif get_part == 2:
    part_two()

if __name__ == "__main__" :
    main()
    