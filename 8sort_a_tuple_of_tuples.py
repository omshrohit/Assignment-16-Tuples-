# write a python program to sort a tuple of tuples by the second item.
tuple1=(('a',21),('b',37),('c',11),('d',29))
list1=[]

for i in range(len(tuple1)):
   list1.append( tuple1[i][::-1])
   
list1.sort()
tuple2=tuple(list1)
print(tuple2)