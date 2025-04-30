from data_handler import load_json, save_json

USERS_FILE = 'users.json'

def register_user():
    users = load_json(USERS_FILE)
    
    name = input("Enter full name: ")
    phone = input("Enter phone number: ")
    national_code = input("Enter national id: ")

    # check for existing user
    for user in users:
        if user['phone'] == phone or user['national_code'] == national_code:
            print("User already registered.")
            return None

    while True:
        try:
            balance = float(input("Enter wallet balance ($100–$1000): "))
            if 100 <= balance <= 1000:
                break
            else:
                print("Amount must be between 100 and 1000.")
        except ValueError:
            print("Please enter a valid number.")

    new_user = {
        "name": name,
        "phone": phone,
        "national_code": national_code,
        "wallet": balance,
        "history": [],
        "reserved_room": None
    }

    users.append(new_user)
    save_json(USERS_FILE, users)
    print("Registration successful. Logged in as", name)
    return new_user


def login_user():
    users = load_json(USERS_FILE)
    phone = input("Enter phone number: ")
    national_code = input("Enter national code: ")

    for user in users:
        if user['phone'] == phone and user['national_code'] == national_code:
            print("Login successful. Welcome,", user['name'])
            return user

    print("Invalid login credentials.")
    return None
