from data_handler import load_json, save_json


USERS_FILE = 'data/users.json'
ROOMS_FILE = 'data/rooms.json'


def view_profile(user):
    print("\n--- Your Profile ---")
    print(f"Name: {user['name']}")
    print(f"phone: {user['phone']}")
    print(f"National Code: {user['national_code']}")
    print(f"Wallet: ${user['wallet']}")
    print(f"Reserved Room: {user.get('reserved_room', 'None')}")
    print("---------------------")


def edit_profile(user):
    users = load_json(USERS_FILE)

    print("\n--- Edit Profile ---")
    name = input(f"Name ({user['name']}): ") or user['name']
    phone = input(f"phone ({user['phone']}): ") or user['phone']
    national_code = input(f"National Code ({user['national_code']}): ") or user['national_code']

    # Update fields
    user['name'] = name
    user['phone'] = phone
    user['national_code'] = national_code

    
    for i, u in enumerate(users):
        if u['phone'] == user['phone']:
            users[i] = user
            break

    save_json(USERS_FILE, users)
    print("Profile updated successfully.")


def recharge_wallet(user):
    users = load_json(USERS_FILE)

    try:
        amount = float(input("Enter amount to add to wallet: "))
        if 0 < amount <= 1000:
            user["wallet"] += amount
            for i, u in enumerate(users):
                if u["phone"] == user["phone"]:
                    users[i] = user
                    break
            save_json(USERS_FILE, users)
            print(f"Wallet updated. New balance: ${user['wallet']}")
        else:
            print("Amount must be between $1 and $1000.")
    except ValueError:
        print("Invalid amount.")
