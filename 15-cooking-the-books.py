#!/usr/bin/env python

class CookTheBooks:

    def __init__(self):
        self.input = "input.txt" # Assigning input file
        self.numbers = []   # Declaring list for numbers
        # Opening input file and assigning lines to list
        try:
            self.numbers = open(self.input, "r").readlines()[1::]
        except (IOError):
            print "Unable to open file %s " % (self.file)	# Unable to open file
            exit()

    # Calculate the highest number
    def highest(self, n):
        # index_max = n.index(max(n))
        # print index_max
        print n
        # n[0], n[index_max] = n[index_max], n[0]
        return n

    # Calculate the lowest number
    def lowest(self, n):

        index_min = n.index(min(r for r in n if r > 0))
        # print index_min

        n[index_min], n[0] = n[0], n[index_min]
        lowest_number = n
        return lowest_number

    # Cooking the books
    def cook(self, numbers):
        i = 0
        for n in numbers[0::]:
            n = list(n)
            n.pop()   # Removing the stupid fucking new line character
            print n
            i += 1
            lowest = "".join(self.lowest(n)).replace("\n", "")
            highest = "".join(self.highest(n)).replace("\n", "")

            print "Case #%s: %s %s" % (i, lowest, highest)



accountant = CookTheBooks()

accountant.cook(accountant.numbers)
