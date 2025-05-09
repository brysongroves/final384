#Bryson Groves
#CS 384 Final
#Hunt The Wumpus

import random

# Create the dodecahedron room structure
cave = {
    1: [2, 5, 6],
    2: [1, 3, 8],
    3: [2, 4, 10],
    4: [3, 5, 12],
    5: [1, 4, 7],
    6: [1, 7, 11],
    7: [5, 6, 8],
    8: [2, 7, 9],
    9: [8, 10, 12],
    10: [3, 9, 11],
    11: [6, 10, 12],
    12: [4, 9, 11]
}

# Make sure Room 1 is safe
available_rooms = [room for room in cave if room != 1]

# Randomly select rooms for pits, bats, and Wumpus (avoiding Room 1)
pit_rooms = random.sample(available_rooms, 2)
bat_rooms = random.sample([room for room in available_rooms if room not in pit_rooms], 2)
wumpus_room = random.choice([room for room in available_rooms if room not in pit_rooms and room not in bat_rooms])

#player starting room
current_room = 1


print("Cave Layout:")
for room, connections in cave.items():
    details = []
    if room in pit_rooms:
        details.append("Bottomless Pit")
    if room in bat_rooms:
        details.append("Super Bats")
    if room == wumpus_room:
        details.append("Wumpus")
    print(f"Room {room} connects to {connections} - {' & '.join(details) if details else 'Empty'}")

print(f"\nYou start in Room {current_room}.\n")


while True:
    # Check if the player is in a dangerous room
    if current_room in pit_rooms:
        print("\nYou fell into a bottomelss pit! GAME OVER.")
        break
    elif current_room in bat_rooms:
        print("\n A super bat took you too a random room!")
        current_room = random.choice(available_rooms)
        continue
    elif current_room == wumpus_room:
        print("\nThe Wumpus saw you and killed you! GAME OVER.")
        break
    
    #shows the possible exits of current room
    print(f"\nYou are in Room {current_room}. Exits lead to: {cave[current_room]}")
    
    while True:
        try:
            next_room = int(input("Enter the room number you want to move to: "))
            if next_room in cave[current_room]:
                current_room = next_room
                break
            else:
                print(f"Room {next_room} is not connected to Room {current_room}. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid room number.")