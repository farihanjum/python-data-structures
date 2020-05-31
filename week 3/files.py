handle = open('test.txt')
count = 0
length = handle.read()
for cheese in handle :
    count+=1
print(count)
print(len(length))
