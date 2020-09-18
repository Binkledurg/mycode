#!/usr/bin/env python3
"""
Just a script for a timer
"""

import time

minutes = float(input("How many minutes do you have for your break? "))

print("\rLets start the timer for your ", minutes, " minute break!", flush=True, end="")

def main(minutes):
    """
    My main function for the code
    """
    seconds = 60
    while minutes > 1:

        time.sleep(2)
        minutes -= 1
        if minutes == 1:
            print(f'\rYou have {minutes} minute remaining before the end of your break!',
                    flush=True, end="")
        else:
            print(f'\rYou have {minutes} minutes remaining before the end of your break!',
                    flush=True, end="")


    while minutes == 1:
        time.sleep(.2)
        seconds -= 1
#    secmessage = (f'\rOnly {seconds} seconds left for your break!', flush=True, end="")
        if seconds == 30:
            print(flush=True)
            print(f'\rOnly {seconds} seconds left!', flush=True, end="")
        if seconds == 0:
            print('\rTime is up! Your break is over!', flush=True, end="")
            break

main(minutes)
