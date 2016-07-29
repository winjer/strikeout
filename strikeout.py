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
    
    def cross_out(self, i):
        assert(i <= self.available)
        assert(i > 0)
        self.available -= i
        self.struck += i

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

    def status(self):
        """ returns 0 if nobody has won. returns 1 if every item has been struck. """
        status = 1
        for r in self.sticks:
            if r.available > 0:
                status = 0
        return status

def read_integer(prompt, min_, max_):
    chosen = -1
    while chosen == -1:
        chosen = raw_input("%s (%d - %d)> " % (prompt, min_, max_))
        try:
            chosen = int(chosen)
        except ValueError:
            chosen = -1
            print "Invalid input"
            continue
        if chosen < min_ or chosen > max_:
            chosen = -1
            print "Invalid input"
    return chosen

def main():
    b = Board(4)
    while b.status() == 0:
        print b
        row = 0
        while row == 0:
            chosen = read_integer("Which row", 1, len(b.sticks))
            if b.sticks[chosen-1].available > 0:
                row = chosen
                number = read_integer("How many", 1, b.sticks[chosen-1].available)
        print "Row", row, "Number", number
        b.sticks[row-1].cross_out(number)

if __name__ == '__main__':
    main()

