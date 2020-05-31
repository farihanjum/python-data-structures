bag = dict()
names=['shifa','rifa','tanim','nabila']
for i in names :
    bag[i] = bag.get(i,0)+1
print(bag)
