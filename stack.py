#stack basics

class fix:

#constructor
    def __init__(self):
       self.items = []

    def push(self, key):
     self.items.append(key)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def printStack(self):
        for items in reversed(self.items):
            print (items)



c = fix()
c.push('A')
c.push('B')
c.push('C')
c.printStack()
