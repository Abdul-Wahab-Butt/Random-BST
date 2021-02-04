# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 10:17:57 2021

@author: 92332
"""

import random as RD

class Node:
    
    def __init__(self, value):
        # p = Priority 
# If you want to insert nodes more than 10000, you have to increase the limit below of randrange.

        self.p = int(RD.randrange(10000))
        self.left = None
        self.right = None
        self.value = value
    

    def _Bubble_Up(self, node, value, p):
        
        '''Private/Main function to Insert the values in a tree'''
        
# If tree is empty then insert the value and set length to 1. 
        if node is None:
            node = Node(value)
            if p:
                node.p = p
                
            node.value = value
            return (1, node)

# If the new value is greater then the root
# then insert it to right 
        elif value > node.value:
            (len, node.right) = self._Bubble_Up(node.right, value, p)
            
# Rotate right to fulfil the heap property (if required) 
            if node.right.p < node.p:
                node = self._Rotate_Right(node)
            return (len, node)

# If the new value is less then the root
# then insert it to left   
        elif value < node.value:
            (len, node.left) = self._Bubble_Up(node.left, value, p)

# Rotate left to fulfil the heap property (if required) 
            if node.left.p < node.p:
                node = self._Rotate_Left(node)
            return (len, node)


    def _Trickle_Down(self, node, value):
        
        '''Private/Main function to remove a value from the tree'''
        
        flag = False
        
# Check whether the value (to be searched) is greater then or less then the root.

        if node is not None:
            if value < node.value:

# If value (to be searched) is less then the root then search for it in left subtree. 
                (flag, node.left) = self._Trickle_Down(node.left, value)
            
            elif value > node.value:

# If value (to be searched) is greater then the root then search for it in right subtree. 
                (flag, node.right) = self._Trickle_Down(node.right, value)
            
            else:
                if node.right is None:
                    return (True, node.left)
                
                if node.left is None:
                    return (True, node.right)
                

                if node.left.p < node.right.p:
                    node = self._Rotate_Left(node)
                else:
                    node = self._Rotate_Right(node)

                if node is not None:
                    (flag, node) = self._Trickle_Down(node, value)
                else:
                    node.left = None
                    
        return (flag, node)


    def _Rotate_Left(self, node):
        
        '''Rotate the tree to left'''
        
# Store left nodes in a variable and then perform rotation.
        x = node.left
        node.left = x.right
        x.right = node
        node = x
        return node
    

    def _Rotate_Right(self, node):
        
        '''Rotate the tree to right'''
        
# Store right nodes in a variable and then perform rotation.
        x = node.right
        node.right = x.left
        x.left = node
        node = x
        return node


'''This is the PUBLIC class'''

class Treap:
    
    def __init__(self):
        
# Initiate 
        self.root = None
        self.len = 0
            
    def Add(self, value):
        
        '''Funtion to add value to the tree'''
        
# Priority is None. Will be assigned randomly in the upper class in BubbleUp function.
        p = None

# Obviously, value cannot be None. As we can't access/search for it later.  
        if value is None:
            return "FALSE - Value cannot be None"
        
# If tree is empty then insert the value as root and set length to 1.     
        if self.root is None:
            self.root = Node(value)
            self.root.value = value
            
            if p:
                self.root.p = p
            self.len = 1
            return "TRUE - Inserted"

# Condition to check whether new key (to be inserted) is in the tree or not.  
        if self._Find_Value(value) == True:

# If found, then terminate the function amd return a message.
            return "FALSE - Value is already in the tree."

#  Tree is not empty and the key is not present in the tree, then insert it. 
        else:
            (length, self.root) = self.root._Bubble_Up(self.root, value, p)
            self.len = self.len + 1
            return "TRUE - Inserted"
      

    def Remove(self, value):
        
        '''Funtion to Delete a value that is in the tree'''

# None value not allowed.  
        if value is None:
            return "FASLE - Value cannot be None"

# If tree is empty, nothing to delete.
        if self.root is None:
            return "FALSE - Tree is Empty"

# Call the delete function.
        else:
            (flag, self.root) = self.root._Trickle_Down(self.root, value)
            
# If found, delete!
            if flag:
                self.len = self.len - 1
                return "TRUE - Removed"
            
# Not, then value is not present in the tree. 
            else:
                return "FALSE - Value not found"
    
        
    def  _Find_Value(self, value):
        
        '''Private/Main Function check whether the value is in the tree or not''' 

# Let x be our root as we do not want our main root to be spoiled. 
        x = self.root

# Check, if value is greater then root then search for it in right subtree, else in left.
# If not found, return False. Else, True. 

        while True:
            if x is None:
                return False
            elif value < x.value:
                x = x.left
            elif value > x.value:
                x = x.right
            else:
                break
        
        return True


    def Search_Value(self, value):
        
        '''Function to find the value is in tree or not'''

# Search value cannot be None. 
        if value is None:
            return "FLASE - Value cannot be None"

# Call the main function. 
        if self._Find_Value(value) == True:
            return "TRUE - Given value found in the tree"
        
        else:
            return "FALSE - Not Found"
     
        
    def Search_Min_Value(self):
        
        '''Function to find the minimum value in the tree'''
        
# Let x be our root as we do not want our main root to be spoiled. 
        x = self.root

        if x is None:
            return "Tree is empty"

# Search for value in left subtree as all the nodes with minimum priority are stored there.
        while x.left is not None:
            x = x.left
        return "Minimum value in the tree is", x.value


    def Search_Max_Value(self):
        
        '''Function to find the maximum value in the tree''' 

# Let x be our root as we do not want our main root to be spoiled. 
        x = self.root

        if x is None:
            return "Tree is empty"
    
# Search for value in right subtree as all the nodes with maximum priority are stored there.
        while x.right is not None:
            x = x.right
        return "Maximum value in the tree is", x.value
    

    def Total_Nodes(self):
        
        '''Return the length/number of nodes present in a tree'''

        return self.len
    