from math import sqrt

type = int(input())

if type == 1: #for parabola
    x1, y1 = input().split(' ')
    x1, y1 = float(x1), float(y1)
    if (x1 != 0):
        p = (y1**2) / (2*x1)
        print('p = ', p)
    else:
        print('WRONG INPUT')

if type == 2: #for hyperbola
    x1, y1 = input().split(' ')
    x2, y2 = input().split(' ')
    x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
    flag = 1
    if (((x1**2) + (x2**2)) != 0):
        b = ((x1**2) * (y2**2) - (x2**2) * (y1**2)) / ((x1**2) + (x2**2))
    else:
        flag = 1
    if ((b + (y1**2)) != 0) and (flag == 0):
        a = b * (x1**2) / (b + (y1**2))
    else:
        flag = 1
    if (a >= 0) and (b >= 0) and (flag == 0):
        print('a = ', sqrt(a), 'b = ', sqrt(b))
    else:
        flag = 1
    if (flag != 0):
        print('WRONG INPUT')

if type == 3: #for ellipse
    x1, y1 = input().split(' ')
    x2, y2 = input().split(' ')
    x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
    flag = 0
    if (((x1**2) - (x2**2)) != 0):
        b = ((x1**2) * (y2**2) - (x2 ** 2) * (y1**2)) / ((x1**2) - (x2**2))
    else:
        flag = 1
    if ((b - (y1**2)) != 0) and (flag == 0):
        a = b * (x1**2) / (b - (y1**2))
    else:
        flag = 1
    if (a >= 0) and (b >= 0) and (flag == 0):
        print('a = ', sqrt(a), 'b = ', sqrt(b))
    else:
        flag = 1
    if (flag != 0):
        print('WRONG INPUT')

