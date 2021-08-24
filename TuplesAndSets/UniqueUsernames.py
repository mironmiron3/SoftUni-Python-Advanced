n = int(input())
usernames = set()
for i in range(n):
    usernames.add(input())
[print(username) for username in usernames]