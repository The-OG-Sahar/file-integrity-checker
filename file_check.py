import os
import hashlib

# Ask for the file
filename = input("Enter a file name: ")

# Check if file exists
if not os.path.exists(filename):
    print("The file does NOT exist.")
else:
    # Open and read file to calculate SHA-256 hash
    with open(filename, "rb") as f:
        file_data = f.read()
        file_hash = hashlib.sha256(file_data).hexdigest()
    print(f"SHA-256 Hash of '{filename}': {file_hash}")
