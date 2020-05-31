stuff = list()

fh = open('romeo.txt')
for line in fh :
    st = line.split()
    for i in st :
        if i not in stuff :
            stuff.append(i)

stuff.sort()
print(stuff)
