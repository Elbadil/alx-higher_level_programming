#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i < j:
            if i != 8 or j != 9:
                print("{0:d}".format(i), end='')
                print("{0:d}".format(j), end=', ')
            else:
                print("{0:d}".format(i) + "{0:d}".format(j))
