current_users = ['nicolas','william','chelsea','helen','tim']
new_users = ['mayer','cindy','vanessa','tim','helen']
current_users_lower = [user.lower() for user in current_users]
for x in new_users:
    if x.lower() in current_users_lower:
        print("Sorry " + x + ", please enter another username.")
    else:
        print("The username " + x + " ,is available")
