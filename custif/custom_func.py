#!/usr/bin/env python3
import csv

# Since we are reading the data in from a file, you should not have this set from user input

# connection = float(input('How many Mbps download speed do you have? '))

def main(connection):
    message = 'Your internet is '
    if connection >= 100:
        message = message + "freakin' fast! I'm so jealous!"
    elif connection >= 50:
        message = message + "pretty decent. About average I would say."
    elif connection >= 25:
        message = message + "better than nothing I suppose"

# Moved connection == 0 here because it is < 24
    elif connection == 0:
        message = "You're really living in the stone ages?"

    elif connection <= 24:
        message = "How do you even survive with this?"

# The following line doesn't work because 0 is < 24 so the previous elif is chosen instead
    elif connection == 0:
        message = "You're really living in the stone ages?"

    else:
        message = "You don't know how fast your internet is? Weak."


# Hang on. New Idea.

# You should create a new function to gather connection speeds and write them to a file
# 
# So I would start like this:
def func_name():
    while True:
#        connection = input("Connection speed or 'quit' when finished. ")
#        if connection.lower() == 'quit':
#            break
#        connection = str(connection)
        with open('speed.csv', 'w', newline = '') as csv_file:
            connection = input("Connection speed or 'quit' when finished. ")
            if connection.lower() == 'quit':
                break
#            connection = str(connection)
            writer = csv.writer(csv_file)
            writer.writerow([connection])

def real_main():
    with open('speed.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

func_name()
real_main()

# main(connection)
