fh = open('mbox-short.txt')
for line in fh :
    if line.startswith('From: ') :
        line = line.rstrip()
        print(line)

count  = 0
fh = open('mbox-short.txt')

#subject : diye koita line start hoise check korte pari
for line in fh :
    if line.startswith('Subject: ') :
        count=count+1
print(count)
#jodi bad file nme dei
try :
    fname  = input('enter file name?')
    fopen= open(fname)

except :
    print("Can't open the file")
    quit()

for line in fopen :
    if line.startswith('From: ') :
        line = line.rstrip()
        print(line)
