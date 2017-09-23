usernames = []
if usernames:
    for x in usernames:
        if x == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello, " + x +" thank you for logging in again!")
else:
    print("We need to find some users")
