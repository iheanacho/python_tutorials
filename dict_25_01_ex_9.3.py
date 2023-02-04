#Exercise 3: Write a program to read through a mail log, 
# build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.


name = input ('enter file name: ')
try:
    handle = open(name)
except:
    print('File cannot be opened', name)
    exit()

email_count = dict()
for line in handle:
    if line.startswith('From '):    #isolating line that with From
        line.rsplit()               #clean out whitespace on RHS
        words = line.split()        #splitting the line into a list of words

        for word in words:
            word = words[1]
            email_count[word] = email_count.get(word, 0) +1
print(email_count)

