#solve palindrome problem:
#feedback: requires user input
#@Winterflower for help

class stack():
    def __init__(self):
        self.item = []

    def push(self, key):
        self.item.append(key)

    def pop(self):
        return self.item.pop()

class queue():
    def __init__(self):
        self.item = []

    def push(self, key):
        self.item.append(key)

    def pop(self):
        return self.item.pop(0)

class checker():
    def __init__(self, word):
        self.word = word
        self.queue = queue()
        self.stack = stack()
    def checker(self):
        for letter in self.word:
            self.queue.push(letter)
            self.stack.push(letter)
        for i in range(len(self.word)):
            if self.stack.pop() != self.queue.pop():
                return False
            else:
                return True

palindrome_checker = checker('MAM')
print (palindrome_checker.checker())




