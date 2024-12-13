#Accessing items
a=[1,2,3,4,5]
print(a[0])

#modifying items
a=[1,2,3,4,5]
a[0]=13
a

#adding items
#append()
a=[1,2,3,4,5]
a.append(6)
a

#insert()
a=[1,2,3,4,5]
a.insert(0,89)
a

#removing items
#remove()
a=[1,2,3,4,5]
a.remove(1)
a

#pop()
a=[1,2,3,4,5]
a.pop(1)
a

#other operations
#len()
a=[1,2,3,4,5]
len(a)

#sort()
a=[1,2,3,4,5]
a.sort()
a

#reverse()
a=[1,2,3,4,5]
a.reverse()
a
#iterating through list
a=[1,2,3,4,5]
for i in a:
  print(i)
