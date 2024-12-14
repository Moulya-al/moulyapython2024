#reading a file
file=open("/content/MOULYA.txt","r")
content=file.read()
print(content)
file.close()

file=open("/content/MOULYA.txt","r")
content=file.readline()
print(content)
file.close()

file=open("/content/MOULYA.txt","r")
content=file.readlines()
print(content)
file.close()

#writing to a file
file=open("/content/MOULYA.txt","w")
file.write("hi,alice!\n")
file.close()

#appending to a file
file=open("/content/MOULYA.txt","a")
file.write("This is appended text.\n")
file.close()

#using 'with' statement
with open("/content/MOULYA.txt","r") as file:
  content=file.read()
  print(content)

#file handling modes
with open("/content/naturepic.jpeg","rb")as file:
  data =file.read()

