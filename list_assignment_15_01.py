#Write a program to read through the mail box data and when you find line that starts with “From”, 
# you will split the line into words using the split function. We are interested in who sent the message, 
# which is the second word on the From line.

#From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

# You will parse the From line and print out the second word for each From line, 
# then you will also count the number of From (not From:) lines and print out a count at the end. 
# This is a good sample output with a few lines removed:

count = 0 
fhand = open('mbox-short.txt')
for line in fhand:
    line.rsplit()                           #cleaning out spaces
                    
    if line.startswith ('From '):
        count = count + 1
        words = line.split()                #splitting lines starting with from into a list of words
        target_word = words[1]
        print (target_word)
print (count)
    
        


