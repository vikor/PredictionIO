import sys
import random
""" Usage:
    Command: $ python file_random.py item.txt file_a 10
    randomly pick 10 lines from the file item.txt and write them to file a
"""

read_file = open(sys.argv[1], 'r')
write_file = open(sys.argv[2], 'w')
number_of_lines = int(sys.argv[3])

def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile):
        if random.randrange(num + 2) : continue
        line = aline
    return line

for i in range(0, number_of_lines):
    line = random_line(read_file)
    #start from beginning again
    read_file.seek(0)
    write_file.write(line)
    print i

print "Finished"


