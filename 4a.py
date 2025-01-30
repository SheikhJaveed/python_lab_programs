def password_operations():
    passwd = {'rahul': 'genius', 'kumar': 'smart', 'ankita': 'intelligent'}
    
    print("1. Print all items")
    print("2. Print all keys")
    print("3. Print all values")
    print("4. Get password of user")
    print("5. Change password")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        print(passwd)
    elif choice == 2:
        print(passwd.keys())
    elif choice == 3:
        print(passwd.values())
    elif choice == 4:
        user = input("Enter username: ")
        print(f"Password: {passwd.get(user, 'User not found')}")
    elif choice == 5:
        user = input("Enter username to change password: ")
        new_password = input("Enter new password: ")
        passwd[user] = new_password
        print(f"Password for {user} changed successfully")
    
password_operations()
