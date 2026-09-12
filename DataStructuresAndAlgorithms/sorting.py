import random
import timeit
import LinkedList
from LinkedList import LinkedList


def timer(n):
    array = (random.randint(0, 1000) for i in range(10**n))
    ll = LinkedList()
    ll.startapp(array)
    times = timeit.repeat(setup="from LinkedList import LinkedList",
                          stmt=f"ll.print_linked_list()", repeat=3, number=10)
    print(f"Minimum execution time for 10^{n}: {min(times)}")


timer(3)
timer(4)
timer(5)
timer(6)
timer(7)
