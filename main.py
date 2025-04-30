from auth import register_user, login_user
print("Hello, welcome to Arian Hotel")
def main_menu():
    
    print("1. Log in")
    print("2. Register")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        user = login_user()
        if user:
            logged_in_menu(user)
    elif choice == '2':
        user = register_user()
        if user:
            logged_in_menu(user)
    elif choice == '3':
        print("Thank you for visiting Arian Hotel.")
        exit()
    else:
        print("Invalid choice.")
        main_menu()


def logged_in_menu(user):
    print("\nWelcome,", user['name'])
    print("1. Room list")
    print("2. View wallet balance")
    print("3. View hotel usage and payment history")
    print("4. Check out from reserved room")
    print("5. Exit")

    # Temporarily wait for user input to go back
    input("Feature under development. Press Enter to return to main menu...")
    main_menu()


if __name__ == "__main__":
    while True:
        main_menu()
