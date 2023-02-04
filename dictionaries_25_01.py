##Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. 
# To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. 
# At the end of the program print out the contents of your dictionary (order does not matter).

category = dict()
entry = input('please enter the filename')
fhand = open(entry)
for line in fhand:
    if line.startswith ('From '):
        line.rsplit()           #cleaning out whitespace on lhs
        words = line.split()    #splitting lines into list of words

        for word in words:
            word = words[2]
            print (word)     # checking that i got the right index
            if word not in category:
                category[word] = 1

            else:
                category[word] += 1

print (category) 