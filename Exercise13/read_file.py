with open('pelican.txt', 'r') as pelican:
    lines = pelican.read()
#lines = open('pelican.txt').read()

#for lines in open('pelican.txt').readlines()

    pelican.seek(0)
    llines = pelican.readlines()

print(lines)