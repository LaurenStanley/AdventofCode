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
    value = amplifiers(sequence,0)
    value_list.append(value)
    value_dict[value] = sequence
  print(value_list)
  maximum_value = max(value_list)
  best_sequence = value_dict[maximum_value]
  return(best_sequence, maximum_value)

def amplifiers(sequence,input_value):
  output_values = []
  i = 0
  j = 0
  while True:
    for i in range(5):
      inputs = parse_data()
      sequence_value = sequence[i]
      if j == 0: 
        input_values = (input_value,sequence_value) 
      if j != 0:
        input_values = (input_value,input_value)
      output_value = IntComputer.interpreter(inputs,input_values)
      print(output_value)
      if output_value == 'Halt':
        return output_values[-1]
        break
      else:
        output_values.append(output_value)
        input_value = output_value
    i = 0
    j += 1

def amplifiers2(sequence,input_value):
  output_values = []
  i = 0
  j = 0
  while True:
    for i in range(5):
      inputs = parse_data()
      sequence_value = sequence[i]
      if j == 0: 
        input_values = (input_value,sequence_value) 
      if j != 0:
        input_values = (input_value,input_value)
      output_value = IntComputer.interpreter(inputs,input_values)
      print(output_value)
      if output_value == 'Halt':
        return output_values[-1]
        break
      else:
        output_values.append(output_value)
        input_value = output_value
    i = 0
    j += 1

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
    