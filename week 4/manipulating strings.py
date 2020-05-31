#concatenating strings
a= [1,2,3]
b= [4,5,6]
c= a+b
print(c)
#slicing using slicing operator
a= a[0:2]
print(a)
x= a[0:2]
print(x)
#creating a list from scratch
stuff = list()
stuff.append('s')
stuff.append('ss')
stuff.append(290)
stuff.append([1,2])
print(stuff)
stuff = stuff.append('s')# soevabe likhle list ta none type hoyejabe. and erpor kaj korbe na,
# list append korte hbe just list.append dilei hbe
print(stuff)
stuff = list()
stuff.append('s')
stuff.append('ss')
stuff.append(290)
stuff.append([1,2])
# to checj if something in te list?
if 'sss' not in stuff :
    print('t')
# stuff.sort() kaj korte na because different type
print(stuff)
print(len(stuff))
inn = [1,2,3,4,5,6,7]
print(sum(inn)/len(inn))
