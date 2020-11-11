data_file = 'Input.txt'

#Reads the text file and splits up information by row
def parse_data():
    f = open(data_file, 'r')
    data = f.read()
    f.close()
    strings = data.split('\n')
    return strings

#Takes the raw orbit information and returns 1. a list of the orbit paris and 2) an dictonary with a list of all the bodies and a spot for their orbital value
def get_body_dict(orbit_list):
  body_list = []
  split_orbit_list = []
  for item in orbit_list:
    items = item.split(')')
    body_list.append(items[1])
    split_orbit_list.append(items)
  body_list.sort()
  body_dict = {"COM": 0}
  for item in body_list:
    body_dict[item] = []
  return body_dict,split_orbit_list

def get_body_dict2(orbit_list):
  body_list = []
  split_orbit_list = []
  for item in orbit_list:
    items = item.split(')')
    body_list.append(items[1])
    split_orbit_list.append(items)
  body_list.sort()
  body_dict = {"COM": []}
  for item in body_list:
    body_dict[item] = []
  return body_dict,split_orbit_list

#Calculate the orbital level of each object and add it to the body dictionary. This essentially works its way outward through the system starting at COM. I am sure there is a better way to do this and if it wasnt 6pm on a friday I would find it.
def calculate_orbit_value(body_dict,orbit_list):
  planets_already_orbited = []
  current_orbitee = 'COM'
  i = 0
  while i < len(orbit_list):
    for item in orbit_list:
      if item[0] == current_orbitee:
        value = body_dict[current_orbitee]+1
        body_dict[item[1]] = value
        i += 1
        #print(i/len(orbit_list))
    planets_already_orbited.append(current_orbitee)
    current_orbitee = get_current_orbitee(orbit_list,planets_already_orbited,current_orbitee)
  return body_dict

#Here's the juicy bit - determine whether an item has already calculate its orbital value
def get_current_orbitee(orbit_list,planets_already_orbited,previous_orbitee):
  for item_past in planets_already_orbited:
    #print('a',item_past)
    for item in orbit_list:
      #print('b',item)
      if item_past == item[0]:
        #print('c',item[1],planets_already_orbited)
        if item[1] not in planets_already_orbited:
          #print('d')
          return item[1]

#Add up the total number of orbitals and indirect orbits
def get_orbit_total(body_list, body_dict):
  total_orbits = 0
  for body in body_list:
    total_orbits += body_dict[body]
  return total_orbits

#Calculates path from COM to you
def calculate_your_path(orbit_list):
  orbitee = 'YOU'
  your_path = []
  while orbitee != 'COM':
    for item in orbit_list:
      if item[1] == orbitee:
        your_path.append(item[0])
        orbitee = item[0]
  your_path.reverse()
  return(your_path)

#Calculates path from COM to SAN
def calculate_santas_path(orbit_list):
  orbitee = 'SAN'
  your_path = []
  while orbitee != 'COM':
    for item in orbit_list:
      if item[1] == orbitee:
        your_path.append(item[0])
        orbitee = item[0]
  your_path.reverse()
  return(your_path)

#Finds point where you and santa diverge and adds the orbital transfers needed to get you 1) back to the divergence point and 2) out to where santa is
def calculate_path_between(your_path,santas_path):
  santas_path_away = []
  direct_path = []
  #Calculate the path after divergence to your location
  for i in range(len(your_path)):
    if your_path[i] != santas_path[i]:
      direct_path.append(your_path[i-1:])
      break
  direct_path = direct_path[0]
  direct_path.reverse()
  #Calculate the path after divergence to where santa is
  for i in range(len(santas_path)):
    if your_path[i] != santas_path[i]:
      santas_path_away = santas_path[i:]
      break
  #Combine lists
  direct_path.extend(santas_path_away)
  return direct_path

#How long is the list of orbital transfers (-1 for inclusive counting)
def calculate_orbital_transfers(direct_path):
  orbital_transfers = len(direct_path) -1
  return orbital_transfers

def part_two(bodies,orbits):
  your_path = calculate_your_path(orbits)
  santas_path = calculate_santas_path(orbits)
  direct_path = calculate_path_between(your_path,santas_path)
  number_of_hops = calculate_orbital_transfers(direct_path)
  print(number_of_hops)

def part_one(bodies,orbits):
  filled_body_dict = calculate_orbit_value(bodies,orbits)
  orbit_total = get_orbit_total(bodies,filled_body_dict)
  print(orbit_total)

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

def main():
  raw_orbits = parse_data()
  bodies,orbits = get_body_dict(raw_orbits)
  get_part = get_section()
  if get_part == 1:
    part_one(bodies, orbits)
  elif get_part == 2:
    part_two(bodies,orbits)


if __name__ == "__main__" :
    main()
