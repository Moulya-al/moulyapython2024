with open("data.txt","w") as file:
  file.write("python is awesome!\n")
with open("data.txt","r") as file:
  print(file.read())
