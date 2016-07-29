#! /usr/bin/env python

from StringIO import StringIO
import sys

class Row:

    def __init__(self, length, maxlength=10):
        self.maxlength = maxlength
        self.available = length
        self.struck = 0

    def __str__(self):
        line = "|"*self.available+"*"*self.struck
        return " "*((2*self.maxlength-len(line))/2)+line

class Board:

    def __init__(self, rows):
        self.sticks = []
        for r in range(1,rows+1):
            length = r*2-1
            self.sticks.append(Row(length, rows+1))

    def __str__(self):
        out = StringIO()
        for i, r in enumerate(self.sticks):
            out.write("%2d %s\n" %(i+1, r))
        return out.getvalue()

def main():
    b = Board(4)
    print b

if __name__ == '__main__':
    main()

