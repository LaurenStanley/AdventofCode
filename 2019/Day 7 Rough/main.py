data_file = 'Input.txt'
from itertools import permutations
import IntComputer

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
    #print(sequence)
    value = run_amplifiers(sequence,0)
    value_list.append(value)
    value_dict[value] = sequence
  #print(value_list)
  maximum_value = max(value_list)
  best_sequence = value_dict[maximum_value]
  return(best_sequence, maximum_value)

def run_amplifiers(sequence,input_value):
  inputsA = parse_data()
  inputsB = parse_data()
  inputsC = parse_data()
  inputsD = parse_data()
  inputsE = parse_data()
  
  iA = 0
  iiiA = 0
  iB = 0
  iiiB = 0
  iC = 0
  iiiC = 0
  iD = 0
  iiiD = 0
  iE = 0
  iiiE = 0

  initial_conditionsA = [sequence[0],0]
  initial_conditionsB = [sequence[1]]
  initial_conditionsC = [sequence[2]]
  initial_conditionsD = [sequence[3]]
  initial_conditionsE = [sequence[4]]

  outputEs = []

  while True:
    outputA,inputsA,iA,iiiA = IntComputer.interpreter(inputsA,initial_conditionsA,iA,iiiA)
    initial_conditionsB.append(outputA)
    outputB,inputsB,iB,iiiB = IntComputer.interpreter(inputsB,initial_conditionsB,iB,iiiB)
    initial_conditionsC.append(outputB)
    outputC,inputsC,iC,iiiC = IntComputer.interpreter(inputsC,initial_conditionsC,iC,iiiC)
    initial_conditionsD.append(outputC)
    outputD,inputsD,iD,iiiD = IntComputer.interpreter(inputsD,initial_conditionsD,iD,iiiD)
    initial_conditionsE.append(outputD)
    outputE,inputsE,iE,iiiE = IntComputer.interpreter(inputsE,initial_conditionsE,iE,iiiE)
    initial_conditionsA.append(outputE)
    outputEs.append(outputE)
    if iE == None:
      return outputEs[-2]



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
    