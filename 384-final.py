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

pit_rooms = random.sample(list(cave.keys()), 2)
