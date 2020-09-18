import time
x = 99
while x > 0:
    # \r means go to the beginning of the line
    # flush=True means to remove the previous line buffer
    print(f'\rYou have {x} minutes left in break', flush=True, end="")
    time.sleep(1)
    x -= 1
