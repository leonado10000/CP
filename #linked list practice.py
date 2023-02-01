#linked list practice

class Node:
    def __init__(self,data):
        self.val = data
        self.nxtref = None

class LL:
    def __init__(self):
        self.head = None
    def prin(self):
        n = self.head
        while(n != None):
            print(n.val)
            n = n.nxtref
    def add(self,data):
        

ll1 = LL()
ll1.head = Node(3)
ll1.head.nxtref = Node(15)
ll1.prin()