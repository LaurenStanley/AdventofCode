data_file = 'Input.txt'
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

def create_blank_list(integers):
  blank = []
  for i in range(1000000):
    blank.append(0)
  for i in range(len(integers)):
    blank[i] = integers[i]
  return blank


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

#def part_two():


def part_one():
  rawinput = parse_data()
  filled_indices = create_blank_list(rawinput)
  integers = IntComputer.interpreter(filled_indices)
  #print(integers)

def main():
  get_part = get_section()
  if get_part == 1:
    part_one()
  #elif get_part == 2:
  #  part_two()

if __name__ == "__main__" :
    main()