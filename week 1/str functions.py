if 'na' in 'banana' :
    print(1)
str= 'banana'
pos = str.find('na')
print(pos)#printsposition of substring if it exists
#else prints -1
pos = str.find('q')
print(pos)#printsposition of substring if it exists
print(str.upper())
print(str.lower())
nstr = 'I am fariha'
nstr = nstr.replace('fariha','Nowroze')
print(nstr)
str= ' ohello '
str= str.strip()
print(str+"s")
#lstrip rstrip right and left side er shitespace remove kre
#strip eksthe duitar kore.
if str.startswith('h') :
    print('yess')
pos = str.find('o')
print(pos)
pos = str.find('o',pos+1)
print(pos)
#find e ekta string dile just oita prothom bar kothay appear hoise
#ota bolbe . ar jodi string ar position di taile oi position thek
#check krbe string er sesh porjnto/na pawa porjnto .
#lets do some slicing
str = str[0:3]#second index -1 porjnto nibe .dont forget this you moron
print(str)
