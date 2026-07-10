list_tuple=[("l1",20),("l2",40),("l3",30),]
list_tuple.sort(key=lambda x:x[1])
for i in list_tuple:
    print(i)
print(list_tuple[0])
print(list_tuple[-1])