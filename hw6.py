#Clay Kynor
#12.8.17
#hw6.py

dictionary = open('engmix.txt')

'''
word = input("Enter a word to check ")

counter = 0

for wrd in dictionary:
    if counter == 0:
        if wrd.strip() == word:
            print(wrd, "is in the dictionary")
            counter += 1
            break
if counter==0:
    print("Your word is not in the dictionary")
'''

'''
num = int(input("Enter the numbered word you would like to look for"))

dictList = []

for word in dictionary:
    dictList.append(word)
print(dictList[num-1])
'''
'''
file = open("input.txt")

for line in file:
    print(line.strip()+'!')
'''

letter = input("Enter a letter: ")
    
num = 0
word = ""
for words in dictionary:
    repeat = words.count(letter)
    if repeat > num:
        num = repeat
        word = words
print(word)
