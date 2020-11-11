data_file = 'Input.txt'
import math

#Get that data, keep it raw to spilt later and write coordinates
def parse_data():
    f = open(data_file, 'r')
    data = f.read()
    f.close()
    print(data)
    return data

#Getting coordinates of every asteroid
def get_asteroid_coordinates(raw):
  raw2 = raw.split('\n')
  coordinate_list = []
  height = len(raw2)
  width = len(raw2[0])
  for i in range(len(raw2)):
    current_row = raw2[i]
    for j in range(len(current_row)):
      coordinate = [j,i]
      if current_row[j] == '#':
        coordinate_list.append(coordinate)
  return(coordinate_list,height,width)

#this is the big guy
def get_visible_asteroids(coordinates):
  #Create a dictionary for all asteroids and the number of other asteroinds they can see
  visible_asteroids_count = {}
  
  #Go through all asteroids
  for current_asteroid in coordinates:
    #Create a blank list for all the slopes and distances to other asteroids
    slope_distance_list = []
    for asteroid in coordinates:
      #Do not proceed if the current asteroid is the same as the current asteroid
      if asteroid != current_asteroid:
        #Calculate slope and distance (see function)
        slope, distance, quadrant = calculate_slope_and_distance(current_asteroid,asteroid)
        #Determine whether this asteroid is visible from the base, or blocks another, returns only visible asteroids
        slope_distance_list = determine_asteroid_overlap(slope,distance,quadrant,slope_distance_list)
      #print(current_asteroid,slope_distance_list)
    #What we want to know is how many asteroids can be seen from current. Add this value to a dictionary with the current asteroids coordinates. (Saved as string, sorry.)
    visible_asteroids = len(slope_distance_list)
    visible_asteroids_count[str(current_asteroid)] = visible_asteroids
  #print(visible_asteroids_count) 
  return(visible_asteroids_count)

#Calculate the slope and distance of each asteroid with respect to the 'current asteroid'
def calculate_slope_and_distance(base,exo):
  #Basic slope calculation
  #print(base,exo)
  rise = exo[1] - base [1]
  run = exo[0] - base [0]
  #print(rise,run)
  if run == 0:
    if exo[1] > base[1]:
      slope = 100000
    #if exo[1] < base[1]:
    else:
      slope = -100000
  elif rise == 0:
    if exo[0] > base[0]:
      slope = 0.000001
    if exo[0] < base[0]:
      slope = -0.000001
  else:
    slope = rise/run 
#Quadrant functionality tells you what the direction of the slope is (possible to get the same slope for an asteroid located on either side of the base) This is not elegant but im pretty sure itll work. Remember vectors? Fuck.
  if exo[0] >= base[0]:
    if exo[1] >= base [1]:
      quadrant = '++'
    elif exo[1] < base[1]:
      quadrant = '+-'
  if exo[0] < base[0]:
    if exo[1] >= base [1]:
      quadrant = '-+'
    elif exo[1] < base[1]:
      quadrant = '--'
    
  #If the slope is vertical, I'll set it to something 'arbitrarily high' rather than program in infinity
  #except ZeroDivisionError:
    
  #Pythagorean hypotenuse calculation for distance
  distance = math.sqrt(rise**2 + run**2)
  return slope, distance, quadrant

#In order to find the visible asteroids (from the base) use the slope and determine whether they are along the same line (since asteroids are very small, they wont block anything not in their immediate line of sight)
def determine_asteroid_overlap(current_slope,current_distance,current_quadrant,preexisting_asteroid_data):
  for existing_asteroid in preexisting_asteroid_data:
    #if the slopes are the same
    if current_slope == existing_asteroid[0] and current_quadrant == existing_asteroid[2]:
      #If the new asteroid is further away, it can't be seen. Return the original list
      if current_distance > existing_asteroid[1]:
        return preexisting_asteroid_data
      #If the new asteroid is closer, it is blocking an older asteroid. Remove that asteroid and replace with this one.
      if current_distance < existing_asteroid[1]:
        preexisting_asteroid_data.remove(existing_asteroid)
        current_data = [current_slope,current_distance,current_quadrant]
        preexisting_asteroid_data.append(current_data)
        return preexisting_asteroid_data
  #If the list completes with no overlap, this asteroid isn't in any others line of sight! Add to list and proceed
  current_data = [current_slope,current_distance,current_quadrant]
  preexisting_asteroid_data.append(current_data)
  return preexisting_asteroid_data

#the so called, best asteroid, will be able to see all the other asteroids (or as many as possible) from its POV.
def get_best_asteroid(asteroid_list):
  max_value = max(asteroid_list.values())  # maximum value
  max_keys = [k for k, v in asteroid_list.items() if v == max_value] 
  print('The asteroid located at', max_keys[0], 'can see', max_value, 'other asteroids. This is more than any other.')
  return(max_keys[0])

#This function calculates the coordinates of the closest position for each vector within the grid (from the home position as established in part one)
def calulcate_laser_directions(home_base,x_range,y_range):
  #print(x_range,y_range)
  x_base = home_base[0]
  y_base = home_base[1]
  xmin = 0 - x_base
  ymin = 0 - y_base
  xmax = x_range - x_base -1
  ymax = y_range - y_base -1
  #print(x_base,y_base)
  #print(xmax,ymax) 
  #print(xmin,ymin)
  vector_list = []
  #First Lase (vertical)
  if ymin != 0:
    coord = [0,-1]
    vector_list.append(coord)
  #First Quadrant
  slope_list = []
  ratio_list = []
  for x in range(0,xmax+1):
    for y in range(ymin,0):
      try:
        ratio = [y/x,x,y]
        if ratio[0] not in ratio_list:
          ratio_list.append(ratio[0])
          slope_list.append(ratio)
        else:
          for item in slope_list:
            if item[0] == ratio[0]:
              item_distance = math.sqrt(item[1]**2 + item[2]**2)
              current_distance = math.sqrt(ratio[1]**2 + ratio[2]**2)
              if current_distance < item_distance:
                slope_list.remove(item)
                slope_list.append(ratio)                
      except ZeroDivisionError:
        ratio = 'Vertical'
  slope_list.sort(key=takeRatio)
  #slope_list.reverse()
  #print(slope_list)
  for slope in slope_list:
    vector = [slope[1],slope[2]]
    vector_list.append(vector)
  #Second Quadrant
  slope_list = []
  ratio_list = []
  for x in range(0,xmax+1):
    for y in range(0,ymax+1):
      try:
        #print(x,y)
        ratio = [y/x,x,y]
        if ratio[0] not in ratio_list:
          ratio_list.append(ratio[0])
          slope_list.append(ratio)
        else:
          for item in slope_list:
            if item[0] == ratio[0]:
              item_distance = math.sqrt(item[1]**2 + item[2]**2)
              current_distance = math.sqrt(ratio[1]**2 + ratio[2]**2)
              if current_distance < item_distance:
                slope_list.remove(item)
                slope_list.append(ratio).append(item)
      except ZeroDivisionError:
        ratio = 'Vertical'
  slope_list.sort(key=takeRatio)
  #slope_list.reverse()
  #print(slope_list)
  for slope in slope_list:
    vector = [slope[1],slope[2]]
    vector_list.append(vector)
  #Bottom Lase
  if ymax != 0:
    coord = [0,1]
    vector_list.append(coord)
  #Third Quadrant
  slope_list = []
  ratio_list = []
  for x in range(xmin,0):
    for y in range(0,ymax+1):
      try:
        ratio = [y/x,x,y]
        if ratio[0] not in ratio_list:
          ratio_list.append(ratio[0])
          slope_list.append(ratio)
        else:
          for item in slope_list:
            if item[0] == ratio[0]:
              item_distance = math.sqrt(item[1]**2 + item[2]**2)
              current_distance = math.sqrt(ratio[1]**2 + ratio[2]**2)
              if current_distance < item_distance:
                slope_list.remove(item)
                slope_list.append(ratio)
      except ZeroDivisionError:
        ratio = 'Vertical'
  slope_list.sort(key=takeRatio)
  #slope_list.reverse()
  #print(slope_list,'\n')
  for slope in slope_list:
    vector = [slope[1],slope[2]]
    vector_list.append(vector)
  #FourthQuadrant
  slope_list = []
  ratio_list = []
  for x in range(xmin,0):
    for y in range(ymin,0):
      try:
        #print(x,y)
        ratio = [y/x,x,y]
        if ratio[0] not in ratio_list:
          ratio_list.append(ratio[0])
          slope_list.append(ratio)
        else:
          for item in slope_list:
            if item[0] == ratio[0]:
              item_distance = math.sqrt(item[1]**2 + item[2]**2)
              current_distance = math.sqrt(ratio[1]**2 + ratio[2]**2)
              if current_distance < item_distance:
                slope_list.remove(item)
                slope_list.append(ratio)
      except ZeroDivisionError:
        ratio = 'Vertical'
  slope_list.sort(key=takeRatio)
  #slope_list.reverse()
  #print(slope_list,'\n')
  for slope in slope_list:
    vector = [slope[1],slope[2]]
    vector_list.append(vector)
  final_list = []
  for vector in vector_list:
    if vector not in final_list:
      final_list.append(vector)
  #print(final_list)
  return(final_list)

#Function to simplify list commands    
def takeRatio(elem):
  return elem[0]

#Puts the asteroid coordinates in terms of coordinates with respect to the home position
def transpose_asteroid_coordinates(coordinates,homebase):
  x_home = homebase[0]
  y_home = homebase[1]
  new_coordinates = []
  for coordinate in coordinates:
    x = coordinate[0]
    y = coordinate[1]
    xnew = x-x_home
    ynew = y - y_home
    new_coordinate = [xnew,ynew]
    new_coordinates.append(new_coordinate)
  return new_coordinates

#LASE ASTEROIDS
def lase(laser_vectors, asteroid_coordinates,home_base,laser_fires):
  for vector in laser_vectors:
    potential_hits = []
    if vector[0] == 0:
      for asteroid in asteroid_coordinates:
        if asteroid[0] == 0:
          #print(asteroid)
          #print(vector)
          if vector[1] > 0 and asteroid[1] > 0:
            potential_hits.append(asteroid)
          if vector[1] < 0 and asteroid[1] < 0:
            potential_hits.append(asteroid)
    else:
      vector_slope = vector[1]/vector[0]
      for asteroid in asteroid_coordinates:
        try:
          asteroid_slope = asteroid[1]/asteroid[0]
          if asteroid_slope == vector_slope:
            if asteroid[0] > 0 and vector[0] > 0:
              potential_hits.append(asteroid)
            if asteroid[0] < 0 and vector[0] < 0:
              potential_hits.append(asteroid)
        except ZeroDivisionError:
          continue
    if len(potential_hits) > 0:
      displacements = []
      for hit in potential_hits:
        #print(potential_hits)
        displacement = math.sqrt(hit[0]**2+hit[1]**2)
        displacements.append(displacement)
      minIndex = displacements.index(min(displacements))
      lased_asteroid = potential_hits[minIndex]
      asteroid_coordinates.remove(lased_asteroid)
      laser_fires += 1
      corrected_x = lased_asteroid[0] + home_base[0]
      corrected_y = lased_asteroid[1] + home_base[1]
      corrected_coordinates = [corrected_x,corrected_y]
      if laser_fires == 200:
        print('The laser has fired', laser_fires,'time(s). It just lased the asteroid at coordinates: ',corrected_coordinates)
  return(asteroid_coordinates,laser_fires)

#LASE MORE THAN ONCE
def laser_pass_manager(laser_vectors, asteroid_coordinates,home_base):
  laser_fires = 0
  while True:
    asteroid_coordinates, laser_fires = lase(laser_vectors,asteroid_coordinates,home_base,laser_fires)
    #print(len(asteroid_coordinates))
    if len(asteroid_coordinates) == 1:
      break

#Home base was passed in as a string, so this changes it back :)
def convert_home_base_to_coordinates(homebase):
  for i in range(len(homebase)):
    if homebase[i] == '[':
      x_start = i+1
    if homebase[i] == ',':
      x_end = i-1
      y_start = i+2
    if homebase[i] == ']':
      y_end = i-1
  x = int(homebase[x_start:x_end+1])
  y = int(homebase[y_start:y_end+1])
  homebase = [x,y]
  return homebase

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
  home_base,coordinates,y_range,x_range = part_one()
  #home_base = [3,8]
  #print(coordinates)
  home_base = convert_home_base_to_coordinates(home_base)
  laser_sweep_vectors = calulcate_laser_directions(home_base,x_range,y_range)
  transposed_asteroids = transpose_asteroid_coordinates(coordinates,home_base)
  laser_pass_manager(laser_sweep_vectors,transposed_asteroids,home_base)

def part_one():
  rawinput = parse_data()
  coordinates,height,width = get_asteroid_coordinates(rawinput)
  asteroid_data = get_visible_asteroids(coordinates)
  best_asteroid = get_best_asteroid(asteroid_data)
  return best_asteroid, coordinates,height,width
  

def main():
  get_part = get_section()
  if get_part == 1:
    part_one()
  elif get_part == 2:
    part_two()

if __name__ == "__main__" :
    main()