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
    body_dict[item] = 0
  return body_dict,split_orbit_list

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
        print(i/len(orbit_list))
    planets_already_orbited.append(current_orbitee)
    current_orbitee = get_current_orbitee2(orbit_list,planets_already_orbited,current_orbitee)

  return body_dict

def get_current_orbitee2(orbit_list,planets_already_orbited,previous_orbitee):
  for item_past in planets_already_orbited:
    #print('a',item_past)
    for item in orbit_list:
      #print('b',item)
      if item_past == item[0]:
        #print('c',item[1],planets_already_orbited)
        if item[1] not in planets_already_orbited:
          #print('d')
          return item[1]

def get_orbit_total(body_list, body_dict):
  total_orbits = 0
  for body in body_list:
    total_orbits += body_dict[body]
  return total_orbits


def main():
  raw_orbits = parse_data()
  bodies,orbits = get_body_dict(raw_orbits)
  filled_body_dict = calculate_orbit_value(bodies,orbits)
  #orbitslevels = get_orbit_level(orbits,bodies)
  orbit_total = get_orbit_total(bodies,filled_body_dict)
  print(orbit_total)

if __name__ == "__main__" :
    main()
