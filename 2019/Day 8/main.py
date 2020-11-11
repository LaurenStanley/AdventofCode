data_file = 'Input.txt'
width = 25
height = 6

def parse_data():
    f = open(data_file, 'r')
    data = f.read()
    f.close()
    data = str(data)
    return data

def split_into_layers(data):
  pixels_per_layer = width*height
  for i in range(0,len(data),pixels_per_layer):
    yield data[i:i+pixels_per_layer]

def split_layers_into_rows(layers):
  layer_number = 0
  layer_list = []
  for layer in layers:
    row_list = []
    layer_number += 1
    print('Layer',layer_number,':')
    for i in range(0,len(layer),width*height):
      for x in range(0,width*height,width):
        print(layer[i+x:i+width+x])
        row_list.append(layer[i+x:i+width+x])
    layer_list.append(row_list)
  return(layer_list)

def most_recent_visible(layer_list):
  visible_layer = [2] * (width*height)
  for j in range(0,len(layer_list),1):
    current_layer = layer_list[j]
    #print(current_layer)
    for i in range(0,len(current_layer),1):
      #print(current_layer[i],visible_layer[i])
      if str(visible_layer[i]) in ['2']:
        if int(current_layer[i]) == 0:
          current_pixel = ' '
        elif int(current_layer[i]) == 1:
          current_pixel = 'X'
        else:
          current_pixel = current_layer[i]
        visible_layer[i] = current_pixel
  return(visible_layer)

def print_visible_layer(visible_layer):  
  for i in range(0,len(visible_layer),width*height):
    for x in range(0,width*height,width):
      row = visible_layer[i+x:i+width+x]
      n = ''.join(row)
      print(n)

def least_zeros(layers):
  diction = {}
  for layer in layers:
    zero_count = 0
    for i in range(len(layer)):
      if int(layer[i])==0:
        zero_count += 1
    diction[layer] = zero_count
  print(diction)
  min_value = min(diction.values())
  min_keys = [k for k, v in diction.items() if v == min_value]
  return(min_keys)

def output_value(least_zero_layer):
  ones = 0
  twos = 0
  for i in range(len(least_zero_layer)):
    print(least_zero_layer[i])
    if int(least_zero_layer[i])== 1:
      ones += 1
    if int(least_zero_layer[i])== 2:
      twos += 1
  print('Output Value: ',ones*twos)
    
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

def part_one():
  data = parse_data()
  layers = split_into_layers(data)
  layers = list(layers)
  least_zero_layer = least_zeros(layers)
  output_value(str(least_zero_layer[0]))

def part_two():
  data = parse_data()
  layers = split_into_layers(data)
  layers = list(layers)
  #row_split_layers = split_layers_into_rows(layers)
  #print(layers)
  visible_layer = most_recent_visible(layers)
  print_visible_layer(visible_layer)

def main():
  #get_part = get_section()
  get_part = 2
  if get_part == 1:
    part_one()
  elif get_part == 2:
    part_two()
  
if __name__ == "__main__" :
    main()