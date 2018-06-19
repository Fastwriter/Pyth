#STUDENT: Daulet Demeuov
#GROUP: EN1-C-04
#TASK:Task1 problem F
#Description: Read corner coordinates of triangle (x1,y1,x2,y2,x3,y3) . Then read (X0,Y0) coordinates of one point.
             #Find and output, if this point inside triangle, or outside, or on the line of triangle.
print('Enter triangle`s parameters:')
A=float(input('X1:'))
B=float(input('Y1:'))
C=float(input('X2:'))
D=float(input('Y2:'))
E=float(input('X3:'))
F=float(input('Y3:'))
print('Enter point coordinates:')
G=float(input('X:'))
H=float(input('Y:'))
d=abs(((C-A)*(F-B)-(E-A)*(D-B))**0.5)
d1=abs(((C-A)*(H-B)-(G-A)*(D-B))**0.5)
d2=abs(((G-A)*(F-B)-(E-A)*(H-B))**0.5)
d3=abs(((C-G)*(F-H)-(E-G)*(D-H))**0.5)
if(d==d1+d2+d3):
    print('point is inside triangle')
else: print('point is outside triangle')
