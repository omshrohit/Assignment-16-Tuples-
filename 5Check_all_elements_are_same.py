# check all the items in the tuple are the same

item=(1,1,1,1,4)
item2=(1,2,3,4)

for i in range(1,len(item)):
    if item[i-1]!=item[i]:
        print("all items are not same")
        break
else:
    print("all elements are same")
