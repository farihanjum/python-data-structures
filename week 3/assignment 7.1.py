fname = input('Enter file name?')
f = open(fname)
for line in f :
    uline = line.upper()
    uline = uline.rstrip()
    print(uline)
