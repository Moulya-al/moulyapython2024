with open("/content/MOULYA.txt") as f:
    line_count = sum(1 for line in f)

print(f"The file has {line_count} lines.")
