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

#player starting room & arrow count
current_room = 1
arrows = 5



for room, connections in cave.items():
    details = []
    if room in pit_rooms:
        details.append("Bottomless Pit")
    if room in bat_rooms:
        details.append("Super Bats")
    if room == wumpus_room:
        details.append("Wumpus")
    

print(f"\nYou start in Room {current_room}.\n")

def move_wumpus(wumpus_room):
    rand = random.randint(1,4)
    if rand > 4:  # 75% chance the Wumpus moves
        new_room = random.choice(cave[wumpus_room])
        print(f"\nYou hear a distant roar as the Wumpus moves from Room {wumpus_room} to Room {new_room}...")
        return new_room
    return wumpus_room




while True:
    
    nearby_rooms = cave[current_room]
    warnings = []

    for room in nearby_rooms:
        if room in pit_rooms:
            warnings.append("I feel a draft.")
        if room in bat_rooms:
            warnings.append("Bats nearby.")
        if room == wumpus_room:
            warnings.append("I smell the wumpus.")

    # Print all the warnings, but avoid duplicates
    for warning in set(warnings):
        print(warning)
        
        
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
    
    action = input("Shoot, Move, or Quit (S-M-Q)? ").strip().lower()
    
    if action == "m":
    
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

    elif action == "s":
        if arrows > 0:
            try:
                # Ask how far to shoot
                distance = int(input("How many rooms do you want to shoot through? (1-5) "))
                if 1 <= distance <= 5:
                    # Start the arrow in the current room
                    arrow_room = current_room
                    
                    # Fire the arrow through the chosen number of rooms
                    for _ in range(distance):
                        
                        #Choose a random connected room for the next step
                        arrow_room = random.choice(cave[arrow_room])
                        
                        # Check if the arrow hits the player
                        if arrow_room == current_room:
                            print("\nYour arrow hit yourself! GAME OVER.")
                            exit(0)
                        if arrow_room == wumpus_room:
                            print("\nYour arrow hit the Wumpus! YOU WIN")
                            exit(0)
                        
            

                    print("\nYour arrow didn't hit anything.")
                    arrows -= 1
                    print(f"You have {arrows} arrows left.")
                else:
                    print("You can only shoot through 1 to 5 rooms.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")
    elif action == "q":
        print(f"You chose to quit, coward.")
        exit(0)
    
    else:
        print("Invalid choice. Please enter M to move, S to shoot, or Q to quit")
        
    if arrows == 0:
        print("\nYou ran out of arrows! GAME OVER.")
        break