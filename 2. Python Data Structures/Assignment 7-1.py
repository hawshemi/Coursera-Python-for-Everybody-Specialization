#Write a program that prompts for a file name, then opens that file and reads through the file,
#and print the contents of the file in upper case.
#Use the file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt
# Use words.txt as the file name


# Prompt the user for a file name
fname = input("Enter file name: ")

# Try to open the file
try:
    fh = open(fname)
except FileNotFoundError:
    print(f"Error: Could not open file {fname}")
    exit(1)

# Read the contents of the file
contents = fh.read()

# Convert the contents to upper case
contents_new = contents.upper().strip()

# Print the upper-case contents to the console
print(contents_new)

# Close the file
fh.close()
