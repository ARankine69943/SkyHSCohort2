with open('pelican.txt','a') as pelican:
    pelican.write('A wonderful bird is a pelican.\nHis bill holds more than his belican.\n')

lines = ['He can take in his beak,\n', 'Enough food for a week,\n', 'But I`m damned if I can see how the helican.\n']

with open('pelican.txt', 'a') as pelican:
    pelican.writelines(lines)

