class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self.stackSize = 0

    def push(self, data):
        temp = Node(data)
        if self.top is None:
            self.top = temp
            self.stackSize = self.stackSize + 1
        else:
            temp.next = self.top
            self.top = temp
            self.stackSize = self.stackSize + 1

    def pop(self):
        try:
            if self.top == None:
                raise Exception("Stack is Empty")
            else:
                temp = self.top
                self.top = self.top.next
                tempdata = temp.data
                self.stackSize = self.stackSize - 1
                del temp
                return tempdata
        except Exception as e:
            print(str(e))

    def isEmpty(self):
        if self.stackSize == 0:
            return True
        else:
            return False

    def size(self):
        return self.stackSize

    def top_element(self):
        try:
            if self.top == None:
                raise Exception("Stack is Empty")
            else:
                return self.top.data
        except Exception as e:
            print(str(e))


s = Stack()
s.push(1)
print(s.size())

s.push(2)
print(s.size())

print(s.pop())
print(s.size())
print(s.pop())
print(s.stackSize)

print(s.top_element())
print(s.isEmpty())
