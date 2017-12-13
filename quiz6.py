#Clay Kynor
#12/13/17
#quiz6.py



#2
dictionary = open("engmix.txt")
total = 0
l = []

for word in dictionary:
    words = word.strip()
    l.append(words)
    if l[0] == 'r':
        total = total + 1
        
print(total)
        


'''
#3
dictionary = open("engmix.txt")
num = int(input("Enter a number"))

for word in dictionary:
    word = word.strip()
    if len(word) == num:
        print(word)
        break
'''

'''
#4
dictionary = open("engmix.txt")
letter = input("Enter a letter")
total = 0

for word in dictionary:
    if letter in word:
        True 
    else:
        total += 1
        
print(total)
'''

'''
#5
dictionary = open("engmix.txt")
myList = []
for word in dictionary:
    myList.append(word)
length = len(myList)
print(myList[((length//2)-1)])
'''