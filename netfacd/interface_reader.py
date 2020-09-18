#!/usr/bin/env python3

import netifaces

address = input("Do you want the MAC or the IP address? ")

# print(netifaces.interfaces())

#for i in netifaces.interfaces():
#    print(f'n***************Details of Interface - {i} *****************')
#    try:
#        print('MAC: ', end='')        
#        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr'])
#        print('IP: ', end='')
#        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr'])
#    except:
#        print('Could not collect adapter information')

def MAC():
    for x in netifaces.interfaces():
        print('MAC: ', end='')
        print((netifaces.ifaddresses(x)[netifaces.AF_LINK])[0]['addr'])

def IP():
    for y in netifaces.interfaces():
        print('IP: ', end='')
        print((netifaces.ifaddresses(y)[netifaces.AF_INET])[0]['addr'])

if address.lower() == "mac":
    MAC()
else:
    IP()



