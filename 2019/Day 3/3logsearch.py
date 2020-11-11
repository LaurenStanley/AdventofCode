data_file = 'WireDiagram.txt'

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
        wireCoordinates = wire_path_by_corners(wire)
        processedWires.append(wireCoordinates)
    return(processedWires)

def wire_path_by_corners(wire):
    cornerList = [[0,0,0]]
    X = 0
    Y = 0
    r = 0
    for direction in wire:
        length = int(direction[1::])                
        if direction[0] =='R':
            X = X + length
            r = r + length
            new_corner = [X,Y,r]
            cornerList.append(new_corner)
        if direction[0] =='L':
            X = X - length
            r = r + length
            new_corner = [X,Y,r]
            cornerList.append(new_corner)
        if direction[0] =='U':
            Y = Y + length
            r = r + length
            new_corner = [X,Y,r]
            cornerList.append(new_corner)
        if direction[0] =='D':
            Y = Y - length
            r = r + length
            new_corner = [X,Y,r]
            cornerList.append(new_corner)
    return(cornerList)

def find_intersections(vertices):
    wire1vertices = vertices[0]
    wire2vertices = vertices[1]
    intersectionpoints = []
    for i in range(len(wire1vertices)-1):
        x1,y1,r1 = wire1vertices[i]
        x2,y2,r2 = wire1vertices[i+1]
        for j in range(len(wire2vertices)-1):
            x3,y3,r3 = wire2vertices[j]
            x4,y4,r4 = wire2vertices[j+1]
            #wire1 is vertical
            if x1 == x2:
                #wire1 travels up, wire2 moves to right
                if y1 <= y3 <= y2 and x3 <= x1 <= x4:
                    x = x1
                    y = y3
                    ra = r1 + y3-y1
                    rb = r3 + x1-x3
                    r = ra + rb
                    intersection = [x,y,r]
                    intersectionpoints.append(intersection)
                #wire1 travels up, 2 going left
                if y1 <= y3 <= y2 and x3 >= x1 >= x4:
                    x = x1
                    y = y3
                    ra = r1 + y3 - y1
                    rb = r3 + x3 - x1
                    r = ra + rb
                    intersection = [x,y,r]
                    intersectionpoints.append(intersection)
                #wire1 travels down, 2 moves right
                if y1 >= y3 >= y2 and x3 <= x1 <= x4:
                    x = x1
                    y = y3
                    ra = r1 - y3 + y1
                    rb = r3 + x1 - x3
                    r = ra + rb
                    intersection = [x,y,r]
                    intersectionpoints.append(intersection)
                # wire 1 travels down, wire2 moves to left
                if y1 >= y3 >= y2 and x3 >= x1 >= x4:
                    x = x1
                    y = y3
                    ra = r1 - y3 + y1
                    rb = r3 - x1 + x3
                    r = ra + rb
                    intersection = [x,y,r]
                    intersectionpoints.append(intersection)
            #wire1 is horizontal
            if y1 == y2:
                #wire1 travels right, w2 up
                if x1 <= x3 <= x2 and y3 <= y1 <= y4:
                    y = y1
                    x = x3
                    ra = r1 + x3 - x1
                    rb = r3 + y1 - y3
                    r = ra + rb
                    intersection = [x,y,r]
                    intersectionpoints.append(intersection)
                #w1 right, wire2 going down
                if x1 <= x3 <= x2 and y3 >= y1 >= y4:
                    y = y1
                    x = x3
                    ra = r1 + x3 - x1
                    rb = r3 + y3 - y1
                    r = ra + rb
                    intersection = [x,y,r]
                    intersectionpoints.append(intersection)
                #wire1 travels left, w2 up
                if x1 >= x3 >= x2 and y3 <= y1 <= y4:
                    y = y1
                    x = x3
                    ra = r1 - x3 + x1
                    rb = r3 + y1 - y3
                    r = ra + rb
                    intersection = [x,y,r]
                    intersectionpoints.append(intersection)
                if x1 >= x3 >= x2 and y3 >= y1 >= y4:
                    y = y1
                    x = x3
                    ra = r1 - x3 + x1
                    rb = r3 + y3 - y1
                    r = ra + rb
                    intersection = [x,y,r]
                    intersectionpoints.append(intersection)
    return(intersectionpoints)    

def closest_point_manhatten(crossPoints):
    distances = []
    for point in crossPoints:
        manhattenDistance = abs(point[0])+abs(point[1])
        if manhattenDistance != 0:
            distances.append(manhattenDistance)
    return(min(distances))

def closest_point_steps(crossPoints):
    distances = []
    for point in crossPoints:
        stepsdistance = point[2]
        if stepsdistance != 0:
            distances.append(stepsdistance)
    return(min(distances))
        
def main():
    rawWires = parse_data()
    processedWires = wire_processor(rawWires)
    crossPoints  = find_intersections(processedWires)
    closestPoint = closest_point_manhatten(crossPoints)
    closestPoint2 = closest_point_steps(crossPoints)
    print(closestPoint,closestPoint2)
    
if __name__== "__main__":
    main()
