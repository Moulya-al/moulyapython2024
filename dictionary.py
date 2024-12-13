g={'name':'moulya','age':18,'marks':100}
g

#accessing
g={'name':'moulya','age':18,'marks':100}
print(g['name'])

#modifying
g={'name':'moulya','age':18,'marks':100}
g['name']='kaveri'
g

#adding
g={'name':'moulya','age':18,'marks':100}
g['gender']='female'
g

#removing
g={'name':'moulya','age':18,'marks':100}
del g['name']
g

#iterating through a dictionary
m={'name':'moulya','age':18,'marks':100}
for key,value in m.items():
  print(key,value)
