fileObj = open('pelican.txt', 'a')
fileObj.write('A wonderful bird is the pelican,')
fileObj.write('\nHis bill holds more than his belican.\n')

lines = ['He can take in his beak,\n', 'Enough food for a week,\n', 'But I\'m damned if I see how the helican.\n']
fileObj.writelines(lines)

fileObj.close()

# \n is required to start each line on a new line