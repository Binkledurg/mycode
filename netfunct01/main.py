#!/usr/bin/env python3


# function to push commands
def commandpush(devicecmd):
    for coffeetime in devicecmd.keys():
        print('Handshaking. .. ... connecting with ' + coffeetime )
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to send command --> ' + mycmds )
            # we'll learn to write code that sends cmds to device here

# Create the command for reloading the device

def devicereboot(devicecmd):
    for coffeetime in devicecmd.keys():
        print("Connecting to.. " + coffeetime + " REBOOTING NOW!")





# start our main script
def main():
    work2do = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}
    # data the replaces data stored in file

    print("Welcome to the network device command pusher")

    ## get data set
    print("\nData set found\n")

    ## run
    commandpush(work2do)
    devicereboot(work2do)

main()

