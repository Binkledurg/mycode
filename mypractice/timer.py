#!/usr/bin/env python3
"""
Just a script for a timer
"""

import time
import datetime
def timer(minutes):
    """
    My main function for the code
    """
    seconds = 60
    # This while loop counts down the minutes until only 1 minute remains
    while minutes > 1:
        time.sleep(2) # Should be 60
        minutes -= 1
        if minutes == 1:
            print(f'\rYou have {minutes} minute remaining before the end of your break!',
                    flush=True, end="")
        else:
            print(f'\rYou have {minutes} minutes remaining before the end of your break!',
                    flush=True, end="")

    """
    This while loop begins counting the seconds once the minutes remaining become 1
    and updates half way through the final minute and finally prints when the timer ends
    """
    while minutes == 1:
        time.sleep(.2)
        seconds -= 1
        if seconds == 30:
            print(flush=True)
            print(f'\rOnly {seconds} seconds left!', flush=True, end="")
        if seconds == 0:
            print('\rTime is up! Your break is over!', flush=True, end="")
            break

def main():
    # Requests user input for timer length
    minutes = float(input("How many minutes do you have for your break? "))
    
    print("\rLets start the timer for your ", minutes, " minute break!", flush=True, end="")
    
    with open("break.log", "a") as f:
         f.write(f"Taking a {minutes} minutes break at {datetime.datetime.now()}\n") 
    timer(minutes)

main()
