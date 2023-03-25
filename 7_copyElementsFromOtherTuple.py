# write a python script to  copy elements 4 and 5 from the following tuple into a new tuple,tuple=(1,2,3,4,5,6)

tuple1=(1,2,3,4,5,6)
new=[i for i in tuple1 if (i==4 or i==5)]
newtuple=tuple(new)
print(newtuple)

