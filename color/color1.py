import crayons


fname = input("What is your first name? ")
lname = input("What is your last name? ")

fcolor = input("red, yellow, or blue? ")
lcolor = input("green, magenta, or cyan? ")

def main(fn, ln, fc, lc):
    if fcolor.lower == "red":
        print(crayons.red(fname, bold=True)
    elif fcolor.lower == "yellow":
        print(crayons.yellow(fname, bold=True)
    elif fcolor.lower == "blue":
        print(crayons.blue(fname, bold=True)


main(fname, lname, fcolor, lcolor)

#print 'red string' in red
print(crayons.red('red string'))

# Red White and Blue text
print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

crayons.disable()
print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

crayons.DISABLE_COLOR = False

# This line will print in color because color is enabled
print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

# print 'red string' in red
print(crayons.red('red string', bold=True))

# print(yellow string' in yellow
print(crayons.yellow('yellow string', bold=True))

# print 'magenta string' in magenta
print(crayons.magenta('magenta string', bold=True))

# print 'white string' in white
print(crayons.white('white string', bold=True))


#main(fname, lname, fcolor, lcolor)
