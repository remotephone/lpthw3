# Import the modules
from sys import argv

# define the arguments. first one is the name of the script
# Second one is the filename you'll work with.
script, filename = argv

# This is where you open the file for reading and assign it to txt
txt = open(filename)

# Print the file name. The f format lets python know to include variables
print(f"Here's your file {filename}:")
# read is a function to.... read a file.
print(txt.read())
txt.close()

# Prompt the user to put the filename in again.
print("Type the filename again:")
file_again = input("> ")

# read the new varaible which equals the filename again.
txt_again = open(file_again)

# Print it again.
print(txt_again.read())
txt_again.close()