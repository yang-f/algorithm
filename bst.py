#! /usr/bin/env python  
import random  
class BTNode:  
    def __init__(self, data, left, right):  
        self.data = data  
        self.left = left  
        self.right = right  
  
  
class BTree:  
    def __init__(self):  
        self.root = None;  
          
    def insert(self, value):  
        self.insertNode(value, self.root)  
          
    def insertNode(self, data, btnode):  
        if btnode == None:  
            btnode = BTNode(data, None, None)  
            self.root = btnode
        elif data < btnode.data:  
            if btnode.left == None:  
                btnode.left = BTNode(data, None, None)  
                return  
              
            self.insertNode(data,btnode.left)  
        elif data >= btnode.data:  
            if btnode.right == None:  
                btnode.right = BTNode(data, None, None)  
                return  
              
            self.insertNode(data,btnode.right)  
  
    def printBTreeImpl(self, btnode):  
        if btnode == None:  
            return  
        self.printBTreeImpl(btnode.left)  
        print btnode.data  
        self.printBTreeImpl(btnode.right) 

    def printBTree(self):  
        self.printBTreeImpl(self.root)  
  
      
  
if __name__ == '__main__':  
      
    btree = BTree() 
    x = [random.randint(0,100) for i in xrange(100)] 
    random.shuffle(x)
    for i in x:  
        btree.insert(i)  
      
    btree.printBTree() 