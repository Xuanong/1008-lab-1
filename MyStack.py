__author__ = 'A88310'

class MyStack:
    def __init__(self):
        self._top = -1
        self._data = []

    def push(self, value):
        self._data.append(value)
        self._top += 1

    def pop(self):
        return self._data.pop()

    def peek(self):
        #---------------Enter your source code here----------------#
        #Return the value of the element at the top of the stack without removing it from the stack
        return self._data[self._top]
        #pass

    def peekAt(self,i):
        #---------------Enter your source code here----------------#
        #Return the value of the element at index i without removing it from the stack
        return self._data[i]
        #pass

    def size(self):
        #---------------Enter your source code here----------------#
        #Return the number of elements in the stack
        return len(self._data)
        #pass

    def copyFrom(self, aStack):
        #---------------Enter your source code here----------------#
        #Copy all the elements from the input stack aStack to this stack
        #overwrite

        #self._data = aStack._data
        for v in range(len(aStack._data)):
            var = aStack.peekAt(v)
            self.push(var)


        #return self._data
        #pass

    def toString(self):
        #---------------Enter your source code here----------------#
        #Return a string representing the content of this stack
        '''
        if MyStack.size(self) > 0:
            stringRep = str(self._data[0])
            for i in range(1, MyStack.size(self)):
                stringRep = str(stringRep) + " " + str(self._data[i])

            return stringRep
        else:
            return ""
        '''


        if self._data > 0:
            return self._data
        else:
            return ""
        #pass

'''
newStack = MyStack()
newStack.push(100)
newStack.push(10)
newStack.push(1)
newStack.push(5)

print newStack.toString()

newStack2 = MyStack()
newStack2.push(20)
newStack2.push(2)
newStack2.push(3)
newStack2.push(4)

print newStack2.toString()
newStack.copyFrom(newStack2)

print newStack.toString()
'''