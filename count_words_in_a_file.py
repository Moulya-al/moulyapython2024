with open("/content/MOULYA.txt", "r") as file:
    content = file.read()
    words = content.split()
    word_count = len(words)

print(f"The file has {word_count} words.")
