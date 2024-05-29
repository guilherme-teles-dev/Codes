#algorithm to say how many flagstone are need to cover the theatre floor
from math import ceil # to my second try, i discover this command and this help me to reduce my big(o) notation.
input = input()
data = input.split()
height = int(data[0])
width = int(data[1])
flagstone = int(data[2])
aheight = flagstone
awidth = flagstone
'''
This is my first try to resolve this problem, but the big(o) notation had been vary awful.
while(aheight < height or awidth < width):
    if aheight < height:
        aheight += flagstone
    if awidth < width:
        awidth += flagstone
numberflagstone = (awidth/flagstone)*(aheight/flagstone)
print(int(numberflagstone))
'''
aheight = ceil(height/flagstone)
awidth = ceil(width/flagstone)
print(aheight*awidth)