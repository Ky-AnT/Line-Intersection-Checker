#Imports the direction module located at 'directionmodule/coordinates.py',
#to figure out the direction of three points
import directionmodule.coordinates as direction
#Gets input of line coordinates
pOne = input('Line one first co-ordinate: ').split()
pTwo = input('Line one second co-ordinate: ').split()
qOne = input('Line two first co-ordinate: ').split()
qTwo = input('Line two second co-ordinate: ').split()
#Checks cases for line intersection, which occur when the direction of 2 points from a line,
#and another point from another line are opposite to each other

getDirA = direction.get_direction([pOne,pTwo,qOne])
getDirB = direction.get_direction([pOne,pTwo,qTwo])
getDirC = direction.get_direction([qOne,qTwo,pOne])
getDirD = direction.get_direction([qOne,qTwo,pTwo])
#print(getDirA,getDirB,getDirC,getDirD)
intersects  = False
#If conditional, which will check if the direction of three chosen points from two lines are opposite to three other
#chosen points from the two lines
#print([pOne,pTwo,qOne,qTwo])
if (getDirA != getDirB) and (getDirC != getDirD):
    #print(f'{getDirA} != {getDirB} and {getDirC} != {getDirD}')
    if getDirA != 'Co-linear' and getDirB != 'Co-linear' and getDirC != 'Co-linear' and getDirD != 'Co-linear':
        print("The lines intersect!")
#If the lines do not intersect, then check for co-lineaif getDirA != getDirB and getDirC != getDirB: print("The lines intersect!"); intersects = Truer line possibilities
else:
    if getDirA == 'Co-linear':
        #If the Q1 point lies on the P line segment
        direction.onLineSegment(direction.Point(pOne[0],pOne[1]),direction.Point(pTwo[0],pTwo[1]),direction.Point(qOne[0],qOne[1]))
    elif getDirB == 'Co-linear':
        #If the Q2 point lies on the P line segment
        direction.onLineSegment(direction.Point(pOne[0],pOne[1]),direction.Point(pTwo[0],pTwo[1]),direction.Point(qTwo[0],qTwo[1]))
    elif getDirC == 'Co-linear':
        #If the P1 point lies on the Q line segment
        direction.onLineSegment(direction.Point(qOne[0],qOne[1]),direction.Point(qTwo[0],qTwo[1]),direction.Point(pOne[0],pOne[1]))
    elif getDirD == 'Co-linear':
        #If the P2 point lies on the Q line segment
        direction.onLineSegment(direction.Point(qOne[0],qOne[1]),direction.Point(qTwo[0],qTwo[1]),direction.Point(pTwo[0],pTwo[1]))
    else:
        print("Lines do not intersect!")



