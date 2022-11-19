class Point:
    def __init__(self,x,y): self.x = x; self.y = y
    def __str__(self): return f'Coords: {self.x}, {self.y}'
def get_direction(coordinates):
    gradient = lambda pointOne, pointTwo: (pointOne.y-pointTwo.y)/(pointOne.x-pointTwo.x)
    #a*d-c*b tells if (a/b) is greater than, less than, or equal to (c/d)
    a = Point(int(coordinates[0][0]),int(coordinates[0][1]))
    b = Point(int(coordinates[1][0]),int(coordinates[1][1]))
    c = Point(int(coordinates[2][0]),int(coordinates[2][1]))
    #print(f'A {a}\nB {b}\nC {c}')
    #acGrad, abGrad = abs(gradient(a,c)), abs(gradient(a,b))
    calculationDifference = (b.y-a.y)*(c.x-b.x)-(c.y-b.y)*(b.x-a.x)
    #print(calculationDifference)
    if calculationDifference > 0:
        #print('Anti-Clockwise')
        return 'Anti-Clockwise'
    elif calculationDifference < 0:
        #print('Clockwise')
        return 'Clockwise'
    else:
        #print('Co-linear')
        return 'Co-linear'
#This method will only be used for the co-linear case
#The method checks whether a point lies on the given line
def onLineSegment(lineA, lineB, pointC):
    if pointC.x <= max(lineA.x,lineB.x) and pointC.x >= min(lineA.x,lineB.x):
        if pointC.y <= max(lineA.y,lineB.y) and pointC.y >= min(lineA.y,lineB.y):
            print("The lines intersect and are co-linear!")
