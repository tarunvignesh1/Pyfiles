#advent of code challenge day3 puzzle 1
data = []
with open('datafileday3.txt') as f:
    data = [x for x in f.read().split()]



#Oxygen rate
i = 0
datacpy = data.copy()
while len(datacpy) > 1:
    zerolist = []
    onelist = []
    zeros = 0
    ones = 0
    for j in range(0,len(datacpy)):

        if datacpy[j][i]=='0':
            zeros+=1
            zerolist.append(datacpy[j])
        else:
            ones+=1
            onelist.append(datacpy[j])

    if zeros> ones:
        datacpy = zerolist
    else:
        datacpy = onelist
    i+=1

oxy = int(datacpy[0],2)

#Co2 rate
i = 0
datacpy = data.copy()
while len(datacpy) > 1:
    zerolist = []
    onelist = []
    zeros = 0
    ones = 0
    for j in range(0,len(datacpy)):

        if datacpy[j][i]=='0':
            zeros+=1
            zerolist.append(datacpy[j])
        else:
            ones +=1
            onelist.append(datacpy[j])

    if ones<zeros:
        datacpy = onelist
    else:
        datacpy = zerolist
    i+=1
    
Co2 = int(datacpy[0],2)

print(Co2*oxy)

