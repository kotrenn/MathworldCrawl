import os, sys, subprocess
from random import *

pages = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
         'H', 'I', 'J', 'K', 'L', 'M', 'N',
         'O', 'P', 'Q', 'R', 'S', 'T', 'U',
         'V', 'W', 'X', 'Y', 'Z', '0']

entries = []
for page in pages:
    with open(page + '.html') as f:
        for line in f:
            if 'file.gif' not in line: continue
            line = line.split('Hyperlink">')[-1]
            line = line.split('</a>')[0]
            entries += [line]

while True:
    shuffle(entries)

    with open('entries.txt', 'w') as f:
        for entry in entries:
            print >>f, entry

    with open('entries.txt', 'r') as f:
        subprocess.call('cscript ptts.vbs', stdin=f)
