#Clay Kynor
#12.7.17
#palindrome.py

file = open('engmix.txt')

for word in file:
    word = word.strip()
    x = list(word)
    x.reverse()
    if x == list(word):
        print(word)