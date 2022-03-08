file = open('pelican.txt', 'r')
contents = file.read()
print(type(contents))
print(contents)
file.close()

# Data type of output = string

# Do you have to repeat this first line in order to put the cursor back to the start? Answer = yes
# But IRL would use the contents variable that I created above (but this isn't what the exercise specified)
file = open('pelican.txt', 'r')
myfilelist = file.readlines()
print('There are', len(myfilelist), 'items in the list.')

# Use a loop to iterate over

# Doesn't work:
# for line in myfilelist:
#     print('\n', line, '\n')

# Works:
# print(''.join(str(line) for line in myfilelist))

# Doesn't work - applying line by line. Line has new line character, so does print function. Printing in loop.
# for line in myfilelist:
#     print(''.join(str(line)))

# This prints number of characters after each list
# import sys
# for line in myfilelist:
#     print(sys.stdout.write(str(line)))

# This does not work
# for line in myfilelist:
#     print(line, sep='')

# This does not work
# for line in myfilelist:
#     print(line, sep='\n')

# Use end not sep
for line in myfilelist:
    print(line, end='')

file.close()