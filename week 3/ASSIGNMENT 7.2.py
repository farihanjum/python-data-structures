fname = input('Enter file name?')
fh = open(fname)
count = 0
total = 0.0
for line in fh :
    if line.startswith('X-DSPAM-Confidence: ') :
        count = count +1
        pos = line.find(': ')
        line = line[pos+2:]
        fstr = float(line)
        total = total+ fstr
ans = total/count
ans = round(ans,12)
print('Average spam confidence:',ans)
