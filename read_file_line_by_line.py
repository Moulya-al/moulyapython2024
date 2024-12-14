file_path = "/content/MOULYA.txt" 

try:
    with open(file_path, "r") as file:
        for line in file:
            print(line, end="") 
except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")
