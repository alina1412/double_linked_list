# Doubly linked list

## What is the project about?

This project is an implementation of a container with an interface of Python `collections.deque` container, and it could be used with the same purpose as a double ended queue.

The container has a doubly linked list data structure, it provides opportunity to `append` and `pop` an element from either end of a list fast.

## Why do I need this project?

I used it in an educational purposes to learn how to work with this data structure, creating classes,  importing  and testing it. It is also a solution of a task from the LeetCode site about [design-linked-list](https://leetcode.com/problems/design-linked-list).
And I used this implementation of a `deque` container for solving another [task](https://leetcode.com/problems/binary-tree-level-order-traversal/), which is shown in demo_usage_of_deque.py

## The structure of the project

The implementation of a `deque` container and testing it located in the folder mycollections/

```py
mycollections/
	+- tests               # pytest for testing 
		+- test_deque.py
		+- test_node.py
	+- __init__.py
	+- deque.py            # class BidirectionalLinkedList
	+- node.py             # class Node
```

The auxiliary TreeNode class was taken from [LeetCode](https://leetcode.com/playground/new/linked-list/) site for the demonstrational task. It is located in the folder leetcode/.
The example of usage of a `deque` container is in the file demo_usage_of_deque.py

```py
leetcode/          
   +- tree.py            # TreeNode class from [LeetCode]

+-demo_usage_of_deque.py
```

## What's in the demo_usage_of_deque.py?

It's a solution for the [task](https://leetcode.com/problems/binary-tree-level-order-traversal/) from LeetCode site with usage of my implementation of a `deque` container. The standard `collections.deque` container has the same interface for the solution, and as it can be used instead, it shows that the result of a usage of my implementation of deque is the same.
