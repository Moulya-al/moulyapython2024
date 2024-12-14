with open("data.txt","a") as file:
  file.write("let's learn file handling.\n")
with open("data.txt","r") as file:
  print(file.read())
