# The implementation of choice for an abstract data type is such as stack is the creation of new class.
# The stack operation is implemented as methods

# Completed Implementation of a stack ADT

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items) - 1]


# Simple Balance Parentheses
"""
Balanced Parentheses:
means that each opening symbol has a corresponding closing symbol and the pairs
of parentheses are properly nested

"""

# ALGORITHM

"""
As you process symbols from left to right, the most recent opening
parenthesis must match the next closing symbol """

"""
Also, the first opening symbol
processed may have to wait until the very last symbol for its match.
"""


def matches(open_, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open_) == closes.index(close)


def par_checker(symbol_string):
    stack = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "({[":
            stack.push(symbol)
            print(symbol)
        else:
            if stack.is_empty():
                balanced = False
                print(symbol)
            else:
                top = stack.pop()
                print(symbol)
                if not matches(top, symbol):
                    balanced = False
                    print(symbol)

        index = index + 1

    if balanced and stack.is_empty():
        return True
    else:
        return False


print(par_checker("[{{}]"))
