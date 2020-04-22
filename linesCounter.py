#!/usr/bin/env python2.7

import os
import re

maxLines = input('Please input the number of the lines which you want to filter:')
fileType = raw_input('Please input which type of file you want to count:')

count = 0
pat = '.' + fileType + '$'
for (root, d, files) in os.walk('./'):
    flag = re.search(r'node_module', root)
    if flag:
        continue

    if not root.endswith('/'):
        root += '/'
    for f in files:
        try:
            isSelf = re.search(pat, f)
            if isSelf:
                temp = open(root + f, 'rU')
                l = len(temp.readlines())
                if l > maxLines:
                    print(root + f, l)
                    count += 1
                temp.close()
        except IOError:
            print(root + f)
            continue

print('The total of the files that lines are more than', maxLines, count)
