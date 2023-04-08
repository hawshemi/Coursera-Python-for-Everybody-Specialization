import re

# read the file contents
filename = "regex_sum_XXXXXX.txt"
with open(filename) as filehandle:
    filecontent = filehandle.read()

# find all the numbers in the file
numbers = re.findall('[0-9]+', filecontent)

# convert the numbers from strings to integers and compute their sum
numbers = [int(num) for num in numbers]
sum_of_numbers = sum(numbers)

# print the sum
print(sum_of_numbers)
