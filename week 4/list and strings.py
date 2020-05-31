#splitting a string
st = 'i am a girl'
bt = st.split()
print(len(bt))
print(bt[1])
for i in bt :
    print(i)
st = 'I;am;a;girl'
bt = st.split()#wont split
print(bt)
bt = st.split(';')#will split
print(bt)
fh = open('mbox-short.txt')
for i in fh :
    if i.startswith('From ') :
        line = i.split()
        nstring = line[1]
        d = nstring.split('@')
        print(d[1])

st[0]='s'
print(st)
