# File Copy with Error Handling

try:
    with open('first.txt', 'r') as firstfile, open('second.txt', 'a') as secondfile:
        for line in firstfile:
            secondfile.write(line)
    print("File copied successfully!")

except FileNotFoundError:
    print("Error: Source file not found!")

except PermissionError:
    print("Error: Permission denied!")

except Exception as e:
    print(f"Error: {e}")
