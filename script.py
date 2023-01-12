import glob
import os
import fileinput

# Set the directory you want to work with
directory = '/path/to/files'

# Set the line you want to replace and the replacement line
old_line = "old_line"
new_line = "new_line"

# Use glob.glob() to get a list of all the files in the directory
for filepath in glob.glob(os.path.join(directory, '*.sql')):
    if os.path.isfile(filepath):
        for line in fileinput.FileInput(filepath, inplace=True):
            print(line.replace(old_line, new_line), end='')
