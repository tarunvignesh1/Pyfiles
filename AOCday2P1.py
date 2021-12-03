#advent of code challenge day2 puzzle 1
from datafile import data;


def position(a):
    n=len(a)
    depth=0
    horizontalpos=0
    for i in range(0,n,2):
        if(a[i]=="up"):
            depth=depth-a[i+1]
        elif a[i]=="forward":
            horizontalpos+=a[i+1]
        elif a[i]=="down":
            depth=depth+a[i+1]
    
    return depth*horizontalpos

print(position(data))
