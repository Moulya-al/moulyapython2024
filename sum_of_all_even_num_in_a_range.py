start=int(input('enter the start of range:'))
end=int(input('enter the end of range:'))
even_sum=0
for i in range(start,end+1):
  if i % 2==0:
    even_sum+=i
print('sum of even number:',even_sum)
