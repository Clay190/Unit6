#Clay Kynor
#12.7.17
#longestShort.py

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z']

longest = 0
word = ""

for words in dictionary:
    length = len(words)
    if length > longest:
        longest = length
        word = words
        
print("The longest word is", word, "with", longest, "characters")
