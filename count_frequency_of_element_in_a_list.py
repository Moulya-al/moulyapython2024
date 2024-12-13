numbers=[1,2,3,4,5,6,7]
frequency={}
for num in numbers:
  frequency[num]=frequency.get(num,0)+1
  print('frequency of elements:',frequency)
