from data_handler import load_json, save_json
from datetime import datetime

USERS_FILE = 'data/users.json'
ROOMS_FILE = 'data/rooms.json'


def show_rooms_by_floor():
    rooms = load_json(ROOMS_FILE)
    print("\nAvailable floors: 1, 2, 3, 4")
    floor = input("Enter floor number: ")

    try:
        floor = int(floor)
        print(f"\nRooms on Floor {floor}:")
        for room_no, room in rooms.items():
            if room["floor"] == floor:
                status = "Available" if room["status"] == "available" else "Reserved"
                print(f"Room {room_no} - ${room['price']} - {status}")
        return floor
    except ValueError:
        print("Invalid floor number.")
        return None


def reserve_room(user):
    rooms = load_json(ROOMS_FILE)
    users = load_json(USERS_FILE)

    floor = show_rooms_by_floor()
    if not floor:
        return

    selected = input("Enter room number to reserve: ")
    room = rooms.get(selected)

    if not room:
        print("Room does not exist.")
        return

    if room["status"] == "reserved":
        print("Room is already reserved.")
        return

    if user["wallet"] < room["price"]:
        print("Not enough balance!")
        print("1. Add balance\n2. Choose another room\n3. Cancel")
        choice = input("Choose: ")
        if choice == '1':
            try:
                amount = float(input("Enter amount to add: "))
                user["wallet"] += amount
                print("Balance updated.")
            except ValueError:
                print("Invalid amount.")
        elif choice == '2':
            return reserve_room(user)
        return

    # Reserve the room
    room["status"] = "reserved"
    user["wallet"] -= room["price"]
    user["reserved_room"] = selected
    user["history"].append({
        "room": selected,
        "price": room["price"],
        "checkin": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  
        "checkout": None
    })

    # Update 
    for i, u in enumerate(users):
        if u["phone"] == user["phone"] and u["national_code"] == user["national_code"]:
            users[i] = user
            break

    save_json(ROOMS_FILE, rooms)
    save_json(USERS_FILE, users)

    print(f"Room {selected} reserved successfully.")

def checkout_room(user):
    rooms = load_json(ROOMS_FILE)
    users = load_json(USERS_FILE)

    reserved_room = user.get("reserved_room")
    if not reserved_room:
        print("You have no room reserved.")
        return

    room = rooms.get(reserved_room)
    if not room:
        print("Room data not found.")
        return

    # Free the room
    room["status"] = "available"
    user["reserved_room"] = None

    # checkout date 
    for entry in reversed(user["history"]):
        if entry["room"] == reserved_room and entry["checkout"] is None:
            entry["checkout"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            break

    
    for i, u in enumerate(users):
        if u["phone"] == user["phone"] and u["national_code"] == user["national_code"]:
            users[i] = user
            break

    # Save updates
    save_json(ROOMS_FILE, rooms)
    save_json(USERS_FILE, users)

    print(f"Successfully checked out of room {reserved_room}.")