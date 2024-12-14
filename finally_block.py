try:
  file=open("example.txt","r")
except FileNotFoundError:
  print("file not found")
finally:
  print("execution complete")
