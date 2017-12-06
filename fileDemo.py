#Clay Kynor
#12/6/17
#fileDemo.py - how to read a file

dicctionary = open('engmix.txt')

wordCount = 0
for word in dicctionary:
    if 'dab' in word:
        print(word.strip())
    wordCount += 1

print('There are', wordCount, "words in the dicctionary")
