### emails.py ###
# Joey Livorno | gil15@pitt.edu | 10.22.2020

# This script contains the python code for a simple email parser. It will function in the following way:
# 1. Receive a string input from the user
# 2. Parse the string for emails using regex
# 3. Return the of list of emails to the user
# 4. Prompt the user for another string
# 5. Exit the program when the user types 'quit'

# Import necessary libraries
import re

# Define expression
email_re = r"\b\w+@\w+.\w{3}\b"

# Welcome
print('\nWelcome to the Email Parser!\n')

# Initial prompt
print('Please enter a string to be parsed.')
text = input()


# Start loop
while (text.lower() != 'quit'):

    # Use re to find email occurences
    emails = set(re.findall(r"\b\w+@\w+\.\w{3}\b", text)) # cast list to set so that there are no duplicates

    #print emails to user
    if len(emails) == 0:
        print('\nThe string you entered did not contain any email addresses.')
    else:
        print('\nWe found the following email addresses:')
        for e in emails:
            print(e)


    # Prompt the user for the string
    print('\nPlease enter another string to be parsed.')
    text = input()

print('\nGoodbye!')
