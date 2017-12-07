#Clay Kynor
#12.7.17
#palindrome.py

file = open('engmix.txt')

for word in file:
    word = word.strip()
    x = word.reverse()
    if x == word:
        print(word)