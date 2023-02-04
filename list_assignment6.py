#Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers 
# at the end when the user enters “done”. Write the program to store the numbers the user enters in a list and use the max() and min() functions
# to compute the maximum and minimum numbers after the loop completes.

lst = list()            #creating empty list
while True:
    inp = input('please enter numbers\n')
    if inp == 'done':
        break
    try:
        num = int(inp)
        lst.append(num)
        maximum = max(lst)
        minimum = min (lst)
        


    except:
        print('enter a number')
print (maximum, minimum)
