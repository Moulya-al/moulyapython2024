def fibonacci(n):
  sequence=[]
  a,b=0,1
  for _ in range(n):
    sequence.append(a)
    a,b=b,a+b
  return sequence

terms=int(input("enter the number of terms:"))
print("Fibonacci sequence:",fibonacci(terms))
