from auth import register, login
from rooms import show_rooms_by_floor, reserve_room, checkout_room
from profile_1 import view_profile, edit_profile, recharge_wallet
import os


if not os.path.exists('data'):
    os.makedirs('data')



    
print("Hello, Welcome to the Arian Azarnioshe online hotel reservation page.\n")
def main_menu():
    print("---------------------")
    print("1. Log in")
    print("2. Register")
    print("3. About us")
    print("4. Exit")
    print("---------------------")
    choice = input("Enter your choice: ")

    if choice == '1':
        user = login()
        if user:
            logged_in_menu(user)
    elif choice == '2':
        user = register()
        if user:
            logged_in_menu(user)
    elif choice == '3':
        print(about_us())
    elif choice == '4':
        print("Thank you for visiting Arian Hotel.")
        exit()
    else:
        print("Invalid choice.")
        main_menu()


def logged_in_menu(user):
    while True:
        print("\nWelcome,", user['name'])
        print("1. Room list")
        print("2. View wallet balance")
        print("3. View hotel usage and payment history")
        print("4. Check out from reserved room")
        print("5. View Profile")
        print("6. Edit Profile")
        print("7. Recharge Wallet")
        print("8. Back to main menu")

        choice = input("Choose: ")

        if choice == '1':
            show_rooms_by_floor()
            reserve = input("Do you want to reserve a room? (y/n): ")
            if reserve.lower() == 'y':
                reserve_room(user)
        elif choice == '2':
            print(f"Wallet Balance: ${user['wallet']}")
        elif choice == '3':
            for h in user['history']:
                print(f"Room {h['room']} - ${h['price']} - Checkin: {h['checkin']} - Checkout: {h.get('checkout', '---')}")
        elif choice == '4':
            checkout_room(user)
        elif choice == '5':
            view_profile(user)
        elif choice == '6':
            edit_profile(user)
        elif choice == '7':
            recharge_wallet(user)
        elif choice == '8':
            break
        else:
            print("Invalid choice.")

def about_us():
    return """\nArian Hotel Booking is an online platform designed to simplify hotel reservations for visitors and students at Islamic Azad University. 
With an intuitive interface, users can browse available accommodations, check rates, and secure their bookings with ease. 
Whether you're looking for short-term stays or extended lodging, Arian Hotel Booking ensures a convenient and reliable experience.\n"""


if __name__ == "__main__":
    while True:
        main_menu()
