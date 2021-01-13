import math
import random
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--items", type = int, help="items to be put")
    parser.add_argument("-r","--radius", type = int, help="radius of the circles")
    parser.add_argument("-min_radius",  type = int, help="minimum radius of random radiuses to be generated")
    parser.add_argument("-max_radius",  type = int, help="maximum radius of random radiuses to be generated")
    parser.add_argument("-b","--boundaries",  type = int,help="boundaries of the space we want to put circles in")
    parser.add_argument("-s","--seed",  type = int, help="seed for the random generator of radiuses")
    parser.add_argument("outputfile",  type = str, help="name of output file")
    args = parser.parse_args()
    print(args)
    return args

def get_boundaries(boundariesfile, boundaries):
    with open(boundariesfile) as f:
        for line in f:
            data = [float(x) for x in line.split()]
            b = Line(data[0], data[1], data[2], data[3])
            boundaries.append(b)
    return boundaries
            
            
def get_random_radiuses(minr, maxr, items):
    rs = []
    for i in range(0,items):
        r = random.randint(minr,maxr)
        rs.append(r)
    return rs

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        
            
def __cmp__(self,other):
    if self.x == other.x and self.y == other.y:
        return 1
    else:
        return 0

class Line:
    def __init__(self, startx, starty, endx, endy):
        self.startx = startx
        self.starty = starty
        self.endx = endx
        self.endy = endy
        
def calculate_distance_from_line(line, circle):
    ux = line.startx
    uy = line.starty
    vx = line.endx
    vy = line.endy
    cx = circle.x
    cy = circle.y
    l2= (ux-vx)^2 + (uy - vy)^2
    if l2 == 0:
        d = (ux - cx)**2 + (uy - cy)**2
        dist = math.sqrt(d)
    else:
        t = (cx - ux)*(vx - ux) + (cy - uy)*(vy - uy)
        t = t / l2
        px = ux + t*(vx - ux)
        py = uy + t*(vy - uy)


    return dist

def find_next_circle(c1, c2, r):
    dx = c2.x - c1.x
    dy = c2.y - c1.y
    d = math.sqrt(dx*dx + dy*dy)    
    r1 = c1.r + r
    r2 = c2.r + r
    l = (r1**2- r2**2 + d**2) / (2* d* d)
    temp = (r1**2/d**2)-l**2
    e = math.sqrt(temp)
    kx = c1.x + l*dx - e*dy
    ky = c1.y + l*dy + e*dx
    kx = round(kx, 2)
    ky = round(ky, 2)
    newCircle = Circle(kx, ky, r)
    return newCircle

def find_circle_distance(start, circle):
    d1 = circle.x - start.x
    dx = (d1)**2
    d2 = circle.y - start.y
    dy = (d2)**2
    d = math.sqrt(dx+dy)
    return d

def find_closest_circle(start, forehead):
    dist = []
    for i in forehead:
        dist.append(find_circle_distance(start, i))
    min_dist = min(dist)
    count = -1
    for j in dist:
        count  = count + 1
        if j == min_dist:
            nearest = j
            pos = count
            break
    return pos 
    
def which_crosses(circle, circles):
    for i in circles:
        dist =  find_circle_distance(i, circle)
        dist = round(dist, 2)
        sum = i.r + circle.r
        if sum < dist:
            crossed = i
        else:
            crossed = -1
        return crossed
    
def check_cross(crossed):
    if (crossed == -1):
        crosses = False
    else:
        crosses = True
    return crosses
    
def is_alive(circle, boundaries):
    for line in boundaries:
        if circle.r <= calculate_distance_from_line(line, circle):
            isAlive = True 
    return isAlive
                
           
            
def circles_finder(circles, items):
    start = circles[0]
    forehead = circles
    counter = 0
    while counter < items:
        closest_pos = find_closest_circle(start, forehead)
        closest = forehead[closest_pos]
        next_to_closest = forehead[closest_pos+1]
        crosses = True
        while crosses:
            candidate = find_next_circle(closest,next_to_closest , r)
            crossed = which_crosses(candidate, circles)
            crosses = check_cross(crossed)
            if crosses == False:
                forehead.append(candidate)
                counter = counter + 1
            else:
                for i in range(0, len(forehead)+ 1):
                    if __cmp__(forehead[i], crossed):
                        cross_pos = i
                    if cross_pos < closest_pos:
                        for i in range (cross_pos+1, closest_pos):
                            forehead.remove(i)
                            closest = crossed
                    else:
                        for i in range (closest_pos+ 1, cross_pos):
                            forehead.remove(i)
                            next_to_closest = crossed
        return forehead


def standard_r_no_boundaries(last_two, items, r):
    i = 0
    while (i < items -2):
        nextCircle =find_next_circle(last_two[0], last_two[1], r)
        exists = False
        for k in circles:
            if __cmp__(k, nextCircle):
                exists = True
        if not exists:
            circles.append(nextCircle)
            last_two[1] = nextCircle
            i = i + 1
        else:
            last_two[0] = nextCircle
        
def random_r_no_boundaries(last_two, items, rs):
    forehead = []
    forehead.append(circles[0])
    forehead.append(circles[1])
    for i in range (2, items):
        nextCircle =find_next_circle(last_two[0], last_two[1], rs[i])
        exists = False
        for k in circles:
            if __cmp__(k, nextCircle):
                exists = True
        if not exists:
            find_closest_circle(circles[0],circles)
            circles.append(nextCircle)
            forehead.append(nextCircle)
            last_two[1] = nextCircle
            
        else:
            last_two[0] = nextCircle
            

    
def write_file(circles, outputfile):
    f = open(outputfile, 'w')
    for i in circles:
        x = str(i.x)
        y = str(i.y)
        r = str(i.r)
        f.write(x + ' '+ y + ' ' + r +'\n')
    f.close()
    return outputfile  
            


args = get_arguments() 

if args.items:
    items = args.items

if (args.boundaries):    
    boundariesfile = args.boundaries
    boundaries = []
    boundaries = get_boundaries(boundariesfile, boundaries)

rs = []
if (args.radius):
    r = args.radius
    for i in range(0, items):
        rs.append(r)
else:
    minr = args.min_radius
    maxr = args.max_radius
    if args.seed:
        random.seed(args.seed)
    rs = get_random_radiuses(minr, maxr, items)
    

start = Circle(0.00,0.00,rs[0])
second_circle = Circle(2*rs[0], 0.00 , rs[1])

circles = []
last_two = []

circles.append(start)
circles.append(second_circle)

last_two.append(start)
last_two.append(second_circle)

if args.items and args.radius:
    standard_r_no_boundaries(last_two, items, r)
elif args.items and not args.radius:
     random_r_no_boundaries(last_two, items, rs)
else:
    circles = circles_finder(circles, items)


#for i in circles:
 #   print(i.x, i.y )
    
outputfile = args.outputfile
write_file(circles, outputfile)






    
    
    
    
    
    
    
    
    
    
    