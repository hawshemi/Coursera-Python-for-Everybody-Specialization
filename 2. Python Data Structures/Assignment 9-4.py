#9.4 Write a program to read through the mbox-short.txt
#and figure out who has the sent the greatest number of mail messages.
#The program looks for 'From ' lines
#and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the
#sender's mail address to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary
#using a maximum loop to find the most prolific committer.


filename = 'mbox-short.txt'

email_count = {}

with open(filename) as file:
    for line in file:
        if line.startswith('From '):
            email = line.split()[1]
            email_count[email] = email_count.get(email, 0) + 1

most_frequent_email = None
max_count = 0

for email, count in email_count.items():
    if count > max_count:
        max_count = count
        most_frequent_email = email

print(most_frequent_email, max_count)
