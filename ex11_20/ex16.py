# import the module
from sys import argv 

# define your args.
script, filename = argv

# Tell the personw hat you're going to do. Give them the chance to not.
print(f"We're going to erase {filename}.")
print("If you don't want taht, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# Prompt for input with ?
input("?")

# open the file for writing. W allows you to write. A allows append.
print("Opening the file...")
target = open(filename, 'w')

# Get rid of what's in the file.
print("Truncating the file. Goodbye!")
target.truncate()

# Prompt the user for 3 lines of text.
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# Write them to the file.
print("I'm going to to write these to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Close the file to save it. 
print("And finally, we close it!")
target.close()