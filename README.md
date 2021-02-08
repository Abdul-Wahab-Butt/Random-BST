# Random-BST
Python implementation of Random Binary Search Tree aka TREAP. (Min Heap)

RANDOM BINARY SEARCH TREE aka TREAP (MIN HEAP)
A Treap (Tree + Heap) store the nodes/numbers in sorted order for an efficient O(logn) lookup. A treap is a combination of randomly binary search tree in which every node holds a value and a priority number that is assigned randomly to every node during insertion.

Following are the properties that every treap must hold:

1.	You parent node(root) should always be smaller then your child nodes. (Min Heap) Your parent node(root) should always be greater then your child nodes. (Max Heap)
2.	Every node should hold a priority number, assigned randomly.
3.	In the left subtree, all the nodes should be smaller then the parent node. In the right subtree, all the nodes should be greater then the parent node.


TIME COMPLEXITY 

INSERT --> O(logn) 
REMOVE --> O(logn) 
SEARCH --> O(logn)

IMPLEMENTATION
This project (Treap) consists of two classes. One is "Node" and the other is "Treap". 

Class "Node" is having all the proivate functions. Like;
1.	_Bubble_Up(node, value, priority)
2.	_Trickle_Down(node, value)
3.	_Rotate_Left(node)
4.	_Rotate_Right(node)

Class "Treap" is having all the public functions. Like;
1.	Add(value)
2.	Remove(value)
3.	Search_Value(value)
4.	Search_Min_Value()
5.	Search_Max_Value()
6.	Total_Nodes()

NOTE: In class "Node", randrange from "random" module is importing only 1 thousand (1000) randomized numbers. So if you want to insert more then 1000 nodes, you have to increase this limit.

