#Clay Kynor
#11/13/17
#longestWord.py - finds the middle word

dicctionary = open('engmix.txt')

total = 0
    
for w in dicctionary:
    num = len(w)
    if num>total:
        total = w

print(total)
