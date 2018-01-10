import math

totaltime = int(input('Enter any number of seconds: '))

hours = int(totaltime/3600)
totaltime = totaltime%3600
minutes = int(totaltime/60)
totaltime = totaltime%60
seconds = totaltime

print(str(hours) + ':' + str(minutes) + ':' + str(seconds))

a = float(input('Enter the edge length of a dodecahedron: '))
area = 3 * math.sqrt(25 + (10 * math.sqrt(5))) * a * a
print (str(area) + 'square units')
