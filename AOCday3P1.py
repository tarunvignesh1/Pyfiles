#advent of code challenge day3 puzzle 1
data = []
with open('datafileday3.txt') as f:
    data = [x for x in f.read().split()]

sizeofdata = len(data)
#print(sizeofdata)
#print(len(data[0]))

gamma_rate = ""
epsilon_rate = ""
bitlist = []
for b in range(0,len(data[0])):
    one = 0
    zero = 0
    for c in range(0,len(data)):
        if data[c][b] == '0':
            zero+=1
        else:
            one+=1

    if zero>one:
        gamma_rate +='0'
        epsilon_rate += '1'
    else:
        gamma_rate +='1'
        epsilon_rate += '0' 

g = int(gamma_rate,2)
e = int(epsilon_rate,2)
print(g*e)


        



