import getsize
import sys
import glob
import os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')
print(pattern)

#: Use the glob.glob() function to obtain the list of filenames

var = glob.glob(pattern)
print(var)

#: use os.path.getsize to find each file's size
for file_name in var:
    if os.path.getsize(file_name) > 0:
        print(os.path.basename(file_name))

    # print(os.path.getsize(file_name))

#: Add a test to only display files that do not have a size of zero
# print(os.path.getsize(file_name))

##: Remove the leading directory name(s) from each filename before you print it - using os.path.basename()
# os.path.basename(file_name)
print(os.path.basename(file_name))
