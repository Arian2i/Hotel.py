import json

rooms = {}
for floor in range(1, 5):  # Floors 1 to 4
    for room in range(1, 4):  # 3 rooms 
        room_number = f"{floor}0{room}"  # name 101, 102, 103...
        rooms[room_number] = {
            "floor": floor,
            "price": floor * 100,
            "status": "available"
        }

with open('rooms.json', 'w') as f:
    json.dump(rooms, f, indent=4)

print("Rooms initialized successfully.")
