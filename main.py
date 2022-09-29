#Jessica
#Exercise-05-Find-the-Point
px = int(input("Enter the point px:"))
py = int(input("Enter the point py:"))
qx = int(input("Enter the point qx:"))
qy = int(input("Enter the point qy:"))

#rx = (2*qx) - px 
#ry = (2*qy) - py

a = 2 * qx
b = 2 * qy
c = a - px
d = b - py


#a = qx-px
#b = qy-py
#c = 2 * a
#d = 2 * b

#result = (2*qx-px,2*qy-py)

print("the point of r = " '(',c,',',d,')')
