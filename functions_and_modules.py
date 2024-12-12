def greet(name):
 print("Hello,"+name+"!")
greet("Alice")

#positional argument
def add(a,b):
  return a+b

print(add(5,3))

#keyword argument
def greet(name,message):
  print(message + "," + name + ",")
greet(name="Alice",message=" good morning")

def sum_numbers(*number):
  return sum(number)
print(sum_numbers(1,2,3,4))

#default argument
def greet(name, message="hello"):
  print(message + "," + name + ",")
greet("Alice")
greet("Bob","hi")

#variable length argument
def sum_numbers(*number):
  return sum(number)
print(sum_numbers(1,2,3,4))
