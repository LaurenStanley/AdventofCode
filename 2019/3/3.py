data_file = 'WireDiagramTest2.txt'

def parse_data():
    f = open(data_file, 'r')
    data = f.read()
    f.close()
    wires = data.split('\n')
    return(wires)

def wire_processor(rawWires):
    processedWires = []
    for wire in rawWires:
        wire = wire.split(',')
        wireCoordinates = wire_path_in_coordinates(wire)
        processedWires.append(wireCoordinates)
    return(processedWires)

def wire_path_in_coordinates(wire):
    coordinateList = [[0,0,0]]
    X = 0
    Y = 0
    r = 0
    for direction in wire:
        length = int(direction[1::])                
        if direction[0] =='R':
            for i in range(length):
                X = X+1
                Y = Y
                r = r+1
                new_coordinate = [X,Y,r]
                coordinateList.append(new_coordinate)
        if direction[0] =='L':
            for i in range(length):
                X = X-1
                Y = Y
                r = r+1
                new_coordinate = [X,Y,r]
                coordinateList.append(new_coordinate)
        if direction[0] =='U':
            for i in range(length):
                X = X
                Y = Y+1
                r = r+1
                new_coordinate = [X,Y,r]
                coordinateList.append(new_coordinate)
        if direction[0] =='D':
            for i in range(length):
                X = X
                Y = Y-1
                r = r+1
                new_coordinate = [X,Y,r]
                coordinateList.append(new_coordinate)
        print(new_coordinate)
    return(coordinateList)


def find_intersection(wireCoordinates):
    wire1 = wireCoordinates[0]
    wire2 = wireCoordinates[1]
    total_combos = len(wire1)*len(wire2)
    combos_tried = 0
    crossPoints = []
    for coordinate1 in wire1:
        for coordinate2 in wire2:
            if coordinate1[0] == coordinate2[0] and coordinate1[1] == coordinate2[1]:
                crossPoints.append([coordinate1,coordinate2])
            combos_tried += 1
        #print(round(combos_tried/total_combos,3))
    return(crossPoints)

def closest_point_manhatten(crossPoints):
    distances = []
    for point in crossPoints:
        wire1coord = point[0]
        wire2coord = point[1]
        manhattenDistance = abs(wire1coord[0])+abs(wire1coord[1])
        if manhattenDistance != 0:
            distances.append(manhattenDistance)
    return(min(distances))

def closest_point_steps(crossPoints):
    distances = []
    for point in crossPoints:
        wire1coord = point[0]
        wire2coord = point[1]
        stepsdistance = abs(wire1coord[2])+abs(wire2coord[2])
        if stepsdistance != 0:
            distances.append(stepsdistance)
    return(min(distances))
        
def main():
    rawWires = parse_data()
    processedWires = wire_processor(rawWires)
    crossPoints  = find_intersection(processedWires)
    print(crossPoints)
    closestPoint = closest_point_steps(crossPoints)
    print(closestPoint)
    
if __name__== "__main__":
    main()
