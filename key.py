key = {'Codingal' : 2,
        'is' : 2,
        'best' : 2, 
        'for' : 2, 
        'Coding' : 1}

print(str(key))

k = 2
count = 0
for i in key:
    if key[i] == k:
        count = count + 1
print("The frequency of 2 is " + str(count))