import random
import os
import time

# Set the screen dimensions
WIDTH = 32
HEIGHT = 14

# Define the player and target symbols
PLAYER = "O"
TARGET = "*"

# Define the game board
board = []
board.append(["_"] * (WIDTH+2))
for i in range(HEIGHT):
    board.append(["|"] + [" "] * WIDTH + ["|"] )
board.append(["-"] * (WIDTH+2))

# Set the player position
player_x = random.randint(1, WIDTH-1)
player_y = random.randint(1, HEIGHT-1)

# Set the target position
target_x = random.randint(1, WIDTH-1)
target_y = random.randint(1, HEIGHT-1)

# Set the score
score = 0

# The game loop
while True:
    # Clear the screen
    os.system('clear')

    # Print the game board
    for i in range(HEIGHT+2):
        print(" ".join(board[i]))

    # Print the score
    print("Score:", score)

    # Move the player
    move = input("Move (w/a/s/d): ")
    if move == "w":
        player_y -= 1
    elif move == "s":
        player_y += 1
    elif move == "a":
        player_x -= 1
    elif move == "d":
        player_x += 1
    elif move == "q":
        break

    # Check if the player is out of bounds
    if player_x < 0:
        player_x = 0
    elif player_x >= WIDTH:
        player_x = WIDTH-1
    elif player_y < 0:
        player_y = 0
    elif player_y >= HEIGHT:
        player_y = HEIGHT-1

    # Check if the player has reached the target
    if player_x == target_x and player_y == target_y:
        score += 1
        target_x = random.randint(0, WIDTH-1)
        target_y = random.randint(0, HEIGHT-1)

    # Update the game board
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if i == player_y and j == player_x:
                board[i][j] = PLAYER
            elif i == target_y and j == target_x:
                board[i][j] = TARGET
            else:
                board[i][j] = " "

    # Wait for a short amount of time before clearing the screen and redrawing the board
    time.sleep(0.1)

    # Clear the screen
    os.system('clear')
