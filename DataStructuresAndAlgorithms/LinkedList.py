import random
import time


class LinkedList:
    def __init__(self):
        self.head = False
        self.tail = False

    class NodeLL:
        def __init__(self, value, link_to_next=False):
            self.value = value
            self.link_to_next = link_to_next

    def startapp(self, *value):
        for val in value:
            if not self.head:
                self.head = self.tail = self.NodeLL(val)
                continue
            self.head = self.NodeLL(val, link_to_next=self.head)

    def endapp(self, *value):
        for val in value:
            if not self.tail:
                self.head = self.tail = self.NodeLL(val)
                continue
            self.tail.link_to_next = self.NodeLL(val)
            self.tail = self.tail.link_to_next

    def serch(self, value):
        if not self.head:
            print("Linked list is empty")
            return False
        ser_n, pre_n, i = self.head, False, 1
        while True:
            if ser_n.value == value:
                print(f"Value {value} on {i} position in Linked list")
                return pre_n
            if not ser_n.value:
                print(f"Value {value} no in Linked list")
                return False
            ser_n, pre_n, i = ser_n.link_to_next, ser_n, i+1

    def print_linked_list(self):
        if not self.head:
            # print("Libked list is empty")
            return
        ser_n = self.head
        while ser_n:
            # print(ser_n.value, end=' ')
            ser_n = ser_n.link_to_next
        # print('\n')

    def delete(self, value):
        point = self.serch(value)
        if not point:
            self.head = self.head.link_to_next
        elif point.link_to_next == self.tail:
            point.link_to_next = False
        elif point:
            point.link_to_next = point.link_to_next.link_to_next
        del point
        print(f"This value was deleted")


def timer(n):
    ll = LinkedList()
    t0 = time.time()
    for i in range(10**n):
        ll.startapp(random.randint(0, 100))
    t1 = time.time()
    ll.print_linked_list()
    t2 = time.time()
    print(f"\nMake array time for 10^{n}: {t1-t0:6f} sec"
          f"\nPrint time for 10^{n}:      {t2-t1:6f} sec")


for i in range(3, 9):
    timer(i)

