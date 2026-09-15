import time
import random


class BinaryTree:

    def __init__(self, root=None):
        self.root_node = root

    class Node:

        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left_node = left
            self.right_node = right

    def AddNode(self, value):

        if self.root_node == None:
            self.root_node = self.Node(value)
            return

        node = self.root_node
        while True:
            if node.value <= value:
                if node.right_node == None:
                    node.right_node = self.Node(value)
                    return
                else:
                    node = node.right_node
            else:
                if node.left_node == None:
                    node.left_node = self.Node(value)
                    return
                else:
                    node = node.left_node

    def PrintTree(self):

        queue, line = [(self.root_node, 0)], 1
        while queue:
            if queue[0][0].left_node != None:
                queue.append((queue[0][0].left_node, queue[0][1] + 1))
            if queue[0][0].right_node != None:
                queue.append((queue[0][0].right_node, queue[0][1] + 1))
            if queue[0][1] == line:
                # print()
                line += 1
            # print(queue[0][0].value, end=' ')
            queue.pop(0)
        # print('\n')
        return line

    def SearchNode(self, value):

        queue, line = [(self.root_node, 0)], 1
        while queue:
            if queue[0][0].left_node != None:
                queue.append((queue[0][0].left_node, queue[0][1] + 1))
            if queue[0][0].right_node != None:
                queue.append((queue[0][0].right_node, queue[0][1] + 1))
            line = line + 1 if queue[0][1] == line else line
            if queue[0][0].value == value:
                print(f'Value {value} on {line} line')
                return
            queue.pop(0)


def timer(n):
    ll = BinaryTree()
    t0 = time.time()
    for _ in range(10**n):
        ll.AddNode(random.randint(0, 100))
    t1 = time.time()
    ll.PrintTree()
    t2 = time.time()
    print(f"\nMake array time for 10^{n}: {t1-t0:6f} sec"
          f"\nPrint time for 10^{n}:      {t2-t1:6f} sec")


for i in range(3, 7):
    timer(i)
