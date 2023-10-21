import numpy as np

class Node:
    def __init__(self, e: object = None):
        self.__data: object = e
        self.__next: Node = None

    def getData(self):
        return self.__data
    
    def setData(self, e: object):
        self.__data = e
    
    def getNext(self):
        return self.__next
    
    def setNext(self, next):
        self.__next = next


class List:
    def __init__(self):
        self.__head: Node = None
        self.__tail: Node = None
        self.__size: int = 0

    def __repr__(self):
        x = ""
        if not self.isEmpty():
            i = self.__head
            while i != None:
                x += f"[{i.getData()}] -> "
                i = i.getNext()
        return x

    def isEmpty(self):
        return self.__size == 0
    
    def getSize(self):
        return self.__size
    
    def setSize(self, s: int):
        self.__size = s
    
    def first(self):
        return self.__head
    
    def last(self):
        return self.__tail
    
    def addFirst(self, e: object):
        n = Node(e)
        if self.isEmpty():
            self.__head = n
            self.__tail = n
            self.__size += 1
        else:
            h = self.__head
            self.__head = n
            n.setNext(h)
            self.__size += 1

    def addLast(self, e: object):
        n = Node(e)
        if self.isEmpty():
            self.__head = n
            self.__tail = n
            self.__size += 1
        else:
            self.__tail.setNext(n)
            self.__tail = n
            self.__size += 1

    def removeFirst(self):
        if not self.isEmpty():
            n = self.__head
            self.__head = n.getNext()
            n.setNext(None)
            self.__size -= 1
            return n
        return None
    
    def removeLast(self):
        if self.__size == 0:
            return None
        elif self.__size == 1:
            self.removeFirst()
        else:
            h = self.__head
            t = self.__tail
            while h.getNext() != t:
                h = h.getNext()
            h.setNext(None)
            self.__tail = h
            self.__size -= 1
            return t
        

class DoubleNode:
    def __init__(self, e: object = None):
        self.__data: object = e
        self.__prev: DoubleNode = None
        self.__next: DoubleNode = None
    
    def getData(self):
        return self.__data

    def setData(self, e: object):
        self.__data = e
    
    def getPrev(self):
        return self.__prev
    
    def setPrev(self, p):
        self.__prev = p

    def getNext(self):
        return self.__next
    
    def setNext(self, n):
        self.__next = n


class DoubleList:
    def __init__(self):
        self.__head: DoubleNode = None
        self.__tail: DoubleNode = None
        self.__size: int = 0
    
    def __repr__(self):
        x = ""
        if not self.isEmpty():
            i = self.__head
            while i != None:
                if i == self.__head:
                    x += "<- "
                x += f"[{i.getData()}]"
                if i.getNext() != None:
                    x += " <-> "
                else:
                    x += " ->"
                i = i.getNext()
        return x

    def isEmpty(self):
        return self.__size == 0
    
    def getSize(self):
        return self.__size
    
    def first(self):
        return self.__head
    
    def last(self):
        return self.__tail
    
    def addFirst(self, e: object):
        n = DoubleNode(e)
        if self.isEmpty():
            self.__head = n
            self.__tail = n
            self.__size += 1
        else:
            h = self.__head
            n.setNext(h)
            h.setPrev(n)
            self.__head = n
            self.__size += 1
    
    def addLast(self, e: object):
        if self.isEmpty():
            self.addFirst(e)
        else:
            n = DoubleNode(e)
            t = self.__tail
            n.setPrev(t)
            t.setNext(n)
            self.__tail = n
            self.__size += 1

    def removeFirst(self):
        if self.isEmpty():
            return None
        else:
            h = self.__head
            self.__head = h.getNext()
            self.__head.setPrev(None)
            h.setNext(None)
            self.__size -= 1
            return h
    
    def removeLast(self):
        if self.isEmpty():
            return None
        else:
            t = self.__tail
            self.__tail= t.getPrev()
            t.setPrev(None)
            self.__tail.setNext(None)
            self.__size -= 1
            return t
        
    def remove(self, n: DoubleNode):
        if n == self.__head:
            return self.removeFirst().getData()
        elif n == self.__tail:
            return self.removeLast().getData()
        else:
            prev = n.getPrev()
            next = n.getNext()
            n.setPrev(None)
            n.setNext(None)
            next.setPrev(prev)
            prev.setNext(next)
            self.__size -= 1
            return n.getData()
        
    def addBefore(self, b: DoubleNode, e: object):
        if b == self.__head:
            self.addFirst(e)
        else:
            n = DoubleNode(e)
            prev = b.getPrev()
            n.setPrev(prev)
            n.setNext(b)
            b.setPrev(n)
            prev.setNext(n)
            self.__size += 1
    
    def addAfter(self, a: DoubleNode, e: object):
        if a == self.__tail:
            self.addLast(e)
        else:
            n = DoubleNode(e)
            next = a.getNext()
            n.setPrev(a)
            n.setNext(next)
            next.setPrev(n)
            a.setNext(n)
            self.__size += 1


class ArrayStack:
    def __init__(self, capacity: int):
        self.__top = -1
        self.__data = np.array([None for i in range(capacity)])

    def __repr__(self):
        x = ""
        if not self.isEmpty():
            i = self.__top
            while i >= 0:
                x += f"{self.__data[i]}"
                if i - 1 >= 0:
                    x += "\n"
                i -= 1
        return x

    def size(self):
        return self.__top + 1
    
    def top(self):
        if self.isEmpty():
            return None
        return self.__data[self.__top]
    
    def isEmpty(self):
        return self.__top == -1

    def push(self, e: object):
        s = self.size()
        if s < len(self.__data):
            self.__data[s] = e
            self.__top += 1
        return "Stack Overflow"
    
    def pop(self):
        if not self.isEmpty():
            e = self.__data[self.__top]
            self.__data[self.__top] = None
            self.__top -= 1
            return e
        return None
    

class Stack:
    def __init__(self):
        self.__data = List()
    
    def __repr__(self):
        x = ""
        if not self.isEmpty():
            t = self.__data.first()
            while t != None:
                x += f"{t.getData()}"
                if t.getNext() != None:
                    x += "\n"
                t = t.getNext()
        return x

    def size(self):
        return self.__data.getSize()

    def top(self):
        if not self.isEmpty():
            return self.__data.first().getData()
        return None
    
    def isEmpty(self):
        return self.size() == 0
    
    def push(self, e: object):
        self.__data.addFirst(e)

    def pop(self):
        if not self.isEmpty():
            return self.__data.removeFirst().getData()
        return None


class ArrayQueue:
    def __init__(self, capacity: int):
        self.__data = np.array([None for i in range(capacity)])
        self.__first = -1
        self.__rear = -1

    def __repr__(self):
        x = ""
        if not self.isEmpty():
            f = self.__first
            i = 1
            while i <= self.size():
                x += f"{i}. {self.__data[f]}"
                if f != self.__rear:
                    x += "\n"
                f = (f + 1) % len(self.__data)
                i += 1
        return x
            

    def size(self):
        return len(self.__data) - (self.__data == None).sum()
    
    def isEmpty(self):
        return self.size() == 0
    
    def first(self):
        return self.__data[self.__first]
    
    def enqueue(self, e: object):
        if self.isEmpty():
            self.__first = (self.__first + 1) % len(self.__data)
            self.__rear = self.__first
            self.__data[self.__rear] = e
        elif self.size() < len(self.__data):
            self.__rear = (self.__rear + 1) % len(self.__data)
            self.__data[self.__rear] = e
        else:
            return "Stack Overflow" 
        
    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            temp = self.__data[self.__first]
            self.__data[self.__first] = None
            self.__first = (self.__first + 1) % len(self.__data)
            return temp
    

class Queue:
    def __init__(self):
        self.__data = List()

    def __repr__(self):
        x = ""
        h = self.__data.first()
        if not self.isEmpty():
            i = 1
            while i <= self.size():
                x += f"{i}. {h.getData()}"
                if h.getNext() != None:
                    x += "\n"
                h = h.getNext()
                i += 1
        return x

    def size(self):
        return self.__data.getSize()

    def isEmpty(self):
        return self.__data.isEmpty()
    
    def first(self):
        if self.isEmpty():
            return None
        return self.__data.first().getData()
    
    def enqueue(self, e: object):
        self.__data.addLast(e)

    def dequeue(self):
        return self.__data.removeFirst()
