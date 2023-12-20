emails = input("Enter email addresses separated by commas: ").split(',')
usernames = []
domains = []
for email in emails:
    parts = email.split('@')
    if len(parts) == 2:
        usernames.append(parts[0])
        domains.append(parts[1])
print("Usernames:", usernames)
print("Domains:", domains)
