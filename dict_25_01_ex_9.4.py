#Exercise 4: Add code to the above program to figure out who has the most messages in the file. 
# After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop
# (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

name = input ('enter file name: ')
try:
    handle = open(name)
except:
    print('File cannot be opened', name)
    exit()

email_count = dict()
for line in handle:
    if line.startswith('From:'):    #isolating line that with From
        line.rsplit()               #clean out whitespace on RHS
        words = line.split()        #splitting the line into a list of words

        for word in words:
            word = words[1]
            email_count[word] = email_count.get(word, 0) +1
print(email_count)

most_msgs = None
values_list = list(email_count.values())
print (values_list)
for value in values_list:
    if most_msgs is None or value > most_msgs:
        most_msgs = value
for email in email_count:
    if most_msgs == email_count[email]:
        right_key = email
print ("Most emails is: ", right_key, most_msgs)
    

"""most_msgs = None
for largest in email_count:
    if most_msgs is None or largest > most_msgs:
        most_msgs=largest
        print (most_msgs)"""
