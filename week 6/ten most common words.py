name = input('Enter file name')
handle = open(name)


firstdict = dict()
for line in handle :
    if line.startswith('From ') :
        line = line.split()
        word = line[1]
        firstdict[word] = firstdict.get(word,0) +1
emp = list()
for key,value in firstdict.items() :
    emp.append((value,key))
emp =sorted(emp,reverse =True )
for i , j in emp[:10] :
    print(j,i)

print(sorted([ (v,k) for k, v in firstdict.items()] ))
