#Clay Kynor
#12.7.17
#reverseFile.py

file = open(""+input('Enter a file: ')+"")

l = []

for line in file:
    l.append(line)

l.reverse()

for i in l:        
    print(i.strip())


    