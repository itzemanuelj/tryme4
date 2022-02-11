# Write your code here :-)
# Write your code here
print('Printing of 9 blank lines')

def nine_lines(): #Function Definition
    print('_')
nine_lines() # Function Call

def three_lines(): #Function Definition
    nine_lines()
    nine_lines()
    nine_lines()
    nine_lines()
    nine_lines()
    nine_lines()
    nine_lines()
    nine_lines()
    nine_lines()
three_lines() # Function Call

def new_lines(): # Function Definition
    print('_') # Calling One Blank Line
new_lines() # Function Call

def clear_screen():
    print('Printing of 25 blank lines')
    three_lines()
    three_lines()
    nine_lines()
    new_lines() # Nested Functions of New Lines to Add
    new_lines()
    new_lines()
    new_lines()
    new_lines()
    new_lines()
nine_lines() #Last line of the program
clear_screen() #Function Call
