from datafile import data

def pos2(a):
    n=len(a)
    depth=0
    horizontalpos=0
    aim=0
    for i in range(0,n,2):
        if(a[i]=="up"):
            aim = aim -a[i+1]
        elif a[i]=="forward":
            horizontalpos+=a[i+1]
            depth = depth+a[i+1]*aim
        elif a[i]=="down":
            aim = aim + a[i+1]
        
    
    return depth*horizontalpos

print(pos2(data))