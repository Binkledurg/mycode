#!/usr/bin/env python3


message = 'Your internet is '

connection = float(input('How many Mbps download speed do you have? '))

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
#elif connection == 0:
#    message = "You're really living in the stone ages?"

else:
    message = "You don't know how fast your internet is? Weak."

print(message)



