"""Exercise 4: Find all unique words in a file

Let’s use Python to achieve that instead. List all unique words, sorted in alphabetical order, 
that are stored in a file romeo.txt containing a subset of Shakespeare’s work.

To get started, download a copy of the file www.py4e.com/code3/romeo.txt. 
Create a list of unique words, which will contain the final result. 
Write a program to open the file romeo.txt and read it line by line. 
For each line, split the line into a list of words using the split function. 
For each word, check to see if the word is already in the list of unique words. 
If the word is not in the list of unique words, add it to the list. 
When the program completes, sort and print the list of unique words in alphabetical order.

"""

unique_words = ['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
'and', 'breaks', 'east', 'envious', 'fair', 'grief',
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
'sun', 'the', 'through', 'what', 'window',
'with', 'yonder']

fhand = open("romeo.txt")
empty_list = list()

for line in fhand:
   every_line = line.split()           #splitting file into lines
   #print(every_line)

   for each_word in every_line:           #traversing through lines 
      if each_word not in empty_list:
         empty_list.append(each_word)
          
      else:
        pass
         
      
   empty_list.sort()
print(empty_list)