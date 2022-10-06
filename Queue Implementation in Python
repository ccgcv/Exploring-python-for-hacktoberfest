class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.queueSize=0
    def enQueue(self,data):
        temp=Node(data)
        if self.front is None:
            self.front=temp
            self.queueSize= self.queueSize+1
        else:
            curr=self.front
            while curr.next!=None:
                curr=curr.next
            curr.next=temp
            self.queueSize=self.queueSize+1
    def deQueue(self):
        try:
            if self.front == None:
                raise Exception("Queue is Empty")
            else:
                temp=self.front
                self.front=self.front.next
                tempdata=temp.data
                self.queueSize= self.queueSize-1
                del temp
                return tempdata
        except Exception as e:
            print(str(e))
    def isEmpty(self):
        if self.queueSize==0:
            return True
        else:
            return False
    def size(self):
        return self.queueSize
    def front_element(self):
        try:
            if self.front == None:
                raise Exception("Queue is Empty")
            else:
                return self.front.data
        except Exception as e:
            print(str(e))
