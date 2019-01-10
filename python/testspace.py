import random

N = 10

list1 = list()
while True:
    if len(list1) == N:
        break
    else:
        curr_num = random.randint(1, N)
        if not curr_num in list1:
            list1.append(curr_num)

list2 = list()
while True:
    if len(list2) == N:
        break
    else:
        curr_num = random.randint(1, N)
        if not curr_num in list2:
            list2.append(curr_num)

print(list1)
print(list2)