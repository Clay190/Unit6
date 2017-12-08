#Clay Kynor
#12.8.17
#hw6.py

dictionary = open('engmix.txt')
'''
word = input("Enter a word to check ")

count = 0
for wrd in dictionary:
    if wrd.strip() == word:
        print(wrd, "is in the dictionary")
        break
    if count==0:
        print("Your word is not in the dictionary")
            
'''

num = int(input("Enter the numbered word you would like to look for"))

dictList = []

for word in dictionary:
    dictList.append(word)
print(dictList[num+1])