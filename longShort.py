#Clay Kynor
#12.7.17
#longestShort.py

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z']
dictionary = open("engmix.txt")

numlong = 0
longest = ""
shortest = ""
numshort = 0

longest = ['']*26

for words in dictionary:
    length = len(words)
    if length > numlong:
        numlong = length
        word = words
        
print("The longest word is", word, "with", numlong, "characters")
