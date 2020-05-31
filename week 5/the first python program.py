name = input('Enter file name')
handle = open(name)
bigcount = None
bigword = None

firstdict = dict()
for line in handle :
    line = line.split()
    for word in line :
         firstdict[word] = firstdict.get(word,0) +1

for key,value in firstdict.items() :
    if bigcount is  None or bigcount < value :
        bigcount = value
        bigword= key
print(bigcount,bigword)
stuff =dict()
print(stuff['candy'])
