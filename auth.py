import json
import os
import hashlib
import random

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if os.path.exists('data/users.json'):
        with open('data/users.json', 'r') as f:
            return json.load(f)
    return []

def save_users(users):
    with open('data/users.json', 'w') as f:
        json.dump(users, f, indent=4)

def generate_otp():
    return str(random.randint(1000, 9999))

def register():
    users = load_users()
    phone = input("Enter your phone number: ")

    
    for user in users:
        if user["phone"] == phone:
            print("This phone number is already registered.")
            return

    otp = generate_otp()
    print(f"Your OTP is: {otp}")  

    user_otp = input("Enter the OTP: ")
    if user_otp != otp:
        print("Invalid OTP.")
        return

    name = input("Enter your full name: ")
    national_code = input("Enter your national ID: ")
    
    
    password = input("Set your password: ")
    hashed_password = hash_password(password)

    
    while True:
        try:
            wallet = int(input("Enter your wallet balance ($100-$1000): "))
            if 100 <= wallet <= 1000:
                break
            else:
                print("Balance must be between 100 and 1000.")
        except ValueError:
            print("Invalid number.")

    user_data = {
        "name": name,
        "phone": phone,
        "password": hashed_password,
        "national_code": national_code,
        "wallet": wallet,
        "reserved_room": None,
        "history": []
    }

    users.append(user_data)
    save_users(users)
    print("Registration successful!")


def login():
    users = load_users()
    phone = input("Enter your phone number: ")
    password = input("Enter your password: ")
    hashed = hash_password(password)

    for user in users:
        if user["phone"] == phone and user["password"] == hashed:
            print("Login successful!")
            return user

    print("Invalid phone number or password.")
    return 
