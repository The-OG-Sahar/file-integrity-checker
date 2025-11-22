import os

filename = input("Enter a file name: ")

if os.path.exists(filename):
    print("The file exists.")
else:
    print("The file does NOT exist.") 
