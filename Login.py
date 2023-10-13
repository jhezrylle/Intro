def login(users):
    while True:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")

        for u in users:
            if username == u[0]:
                if password == u[1]:
                    return username
        print("Username or password is incorrect. Please try again!")


users = [['mon', 'abc123'],['ash','def456'],['ken','ghi789']]
username = login(users)


print(username, "has logged in")