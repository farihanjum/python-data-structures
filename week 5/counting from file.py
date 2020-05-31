#counting words form a input
bag = dict()
line= input('enter your line')
line = line.split()
for i in line :
    bag[i] = bag.get(i,0) + 1
print(bag)
#printing from dictionary
for i in bag :
    print(i, bag[i])

#amra dict thek list e nite pari ,jeta key bade jusr list dbe
jjj = {'shifa': 3 ,'Rifa' : 33, 'Tanim' : 43 }
dictitems= jjj.items()
print(jjj.items())
#items er output jodi kheyal kori amra dekhbo j
#output ta ekta list hishbe ashe jekhne list er protita element holo ek ekta tuple .
dictvalues= jjj.values()
print(dictvalues)
dictkeys = jjj.keys()
print(dictkeys)
listdict=list(jjj)
print(listdict)
for i,j in dictitems :# or we can write for i,j in jjj.items() :
    print(i,j)
