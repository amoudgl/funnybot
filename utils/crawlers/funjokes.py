import csv
import sys

def parse_joke(line):
    # chop off sql command
    line = line[31:].rstrip().strip()[1:-2]
    x = line.split(",")
    # ignore first two elements, merge rest
    ans = ''
    for i in xrange(2, len(x)):
        ans = ans + x[i]
    # remove redundant chars
    ans = ans.replace('\\n', ' ').replace('\\r', '').replace("  ", " ").rstrip().strip()
    # remove quotes
    ans = ans.replace("\'\'", "'").replace("\'","'") 
    ans = ans[1:-1]
    return ans

f = open("../../data/funjokes.sql")
lines = f.readlines()
f.close()
filepath = '../../data/funjokes.csv'
f = open(filepath, 'a')
f.write("S.No.,Jokes\n")
totaljokes = 0 
for i in xrange(len(lines)):
     totaljokes += 1
     f.write(str(totaljokes)+ "," + parse_joke(lines[i]) + "\n")
f.close()

