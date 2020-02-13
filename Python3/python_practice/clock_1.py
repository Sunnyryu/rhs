def clock(x,y):
    hour_1 = (360/12 * float(x) + (360*float(y)/12/60))
    minute_1 = (360/60 * float(y))
    deg_1 = abs(hour_1 - minute_1)
    return deg_1

b = clock(3, 15)
print(b)

