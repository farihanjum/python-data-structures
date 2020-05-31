fname  = input('enter your file name')
handle = open(fname)
dic= dict()
for line in handle :
    if not line.startswith('From ') :
        continue
    line= line.rstrip()
    words= line.split()
    dates= words[5]
    date = dates.split(':')
    hour = date[0]
    dic[hour] = dic.get(hour,0)+1
#print(sorted ([(v,k) for v,k in dic.items()]))
for k,v in sorted(dic.items()) :
    print(k,v)
