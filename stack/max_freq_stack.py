class MaxFreq:
    def __init__(self):
        self.count = {}
        self.stacks = {}
        self.max_count = 0

    def push(self,val):
        valCount = self.count.get(val,0) + 1
        self.count[val] = valCount
        if valCount > self.max_count:
            self.max_count = valCount
            self.stacks[valCount] = []
        self.stacks[valCount].append(val)
    
    def pop(self):
        res = self.stacks[self.max_count].pop()
        self.count[res] -= 1
        if not self.stacks[self.max_count]:
            self.max_count -= 1
        return res
    
freqStack = MaxFreq()
freqStack.push(5)
freqStack.push(7)
freqStack.push(5)
freqStack.push(7)
freqStack.push(4)
freqStack.push(5)
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())
