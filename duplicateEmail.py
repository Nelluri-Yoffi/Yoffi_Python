person = [
    {'id': 1, 'email': 'a@b.com'},
    {'id': 2, 'email': 'c@d.com'},
    {'id': 3, 'email': 'a@b.com'}
]
count = {}
for row in person:
    email = row['email']
    if email in count:
        count[email] = count[email] + 1
    else:
        count[email] = 1
result = []
for email in count:
    if count[email] > 1:
        result.append(email)
print("Email")
for email in result:
    print(email)