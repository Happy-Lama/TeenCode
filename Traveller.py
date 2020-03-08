""" This is a program that gets the shortest route that is viable to reach a particular point.
The points/Towns are specified using a coordiante system and the shortest distance between them computed by vector addition.
And prints the corresponding routes leading to the destination"""
#initailly we import squareroot function form the math module
from math import sqrt
Towns = ['A','B','C','D','E']
Coordinates = [[0,0],[2,3],[4,3],[-1,-2],[12,13]]
Allowed_Routes = ['A=>B','B=>C','C=>D','D=>E','C=>E','B=>D']
#then we define the function Dist(a) which calculates the distance between to speccified towns in the Allowed_Routes and returns the distance rounded to 2 decimal places
def Dist(a):
    Town1 = Allowed_Routes[Allowed_Routes.index(a)][0]
    Town2 = Allowed_Routes[Allowed_Routes.index(a)][3]
    x = Coordinates[Towns.index(Town1)][0] - Coordinates[Towns.index(Town2)][0]
    y = Coordinates[Towns.index(Town1)][1] - Coordinates[Towns.index(Town2)][1]
    Distance = sqrt(x**2 + y**2)
    return round(Distance,2)
#Then we define the function Shortest_Routes(a) which returns the shortest route between two towns and the corresponding distances
def Shortest_Routes(a):
    if (a in Allowed_Routes) == True:
        print(a)
        print( Dist(a))
    else:
        for i in Allowed_Routes:
            if i.find(a[0]) == 0:
                print(i)
                Route = i
                Dist(Route)
        if Route[3] != a[3]:
            Route_alternate = Route[3] + a[1:]
            print(Dist(Route))
            return Shortest_Routes(Route_alternate)
        else:
            print(Dist(Route))
Shortest_Routes('A=>E')