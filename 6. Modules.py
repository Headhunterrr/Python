# ----------------------------------------------------------------------------

# модули

from itertools import zip_longest

n, k = map(int, input().split())
list_n = list(map(int, input().split()))
sum1, k1 = int(0), int(0)

list_n = [[int(aij) for aij in reversed(str(ai))] for ai in list_n]
list_n = list(zip_longest(*list_n, fillvalue=0))
list_n = [[aij for aij in sorted(ai)] for ai in list_n]
for ai in reversed(list_n):
    for aij in ai:
        if aij != 0 and aij != 9:
            if k1 >= k:
                break
            sum1 += (9 - aij)*(10**list_n.index(ai))
            k1 += 1
with open("sum.txt", "w", encoding="utf-8") as f:
    f.write(str(sum1))
