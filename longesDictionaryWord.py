#Clay Kynor
#11/13/17
#longestWord.py - finds the middle word

dictionary = open('engmix.txt')

total = 0
word = ''
    
for w in dictionary:
    num = len(w.strip())
    if len(w.strip())>total:
        total = num
        word = w

print(word, "is the longest word")