dd= {'aa':2 , 'bb':3 , 'cc': 44, 'ff' : 6}
l= list()
for i,v in dd.items() :
    l.append((v,i))
l = sorted(l)
print(l)
l = sorted(l,reverse =True)
print(l)
