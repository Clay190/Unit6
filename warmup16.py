#Clay Kynor
#12.11.17
#warmup.py - Find all the words in the dictionary that start with your first initial and end with your last

dictionary = open('engmix.txt')

for word in dictionary:
    if word != '':
        if word.strip()[0] == 'b':
            if word.strip()[-1] == 'b':
                print(word.strip())
               