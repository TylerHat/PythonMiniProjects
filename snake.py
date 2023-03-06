import numpy as np
import matplotlib.pyplot as plt

# Set up the game board
board_size = 20
board = np.zeros((board_size, board_size))
player_pos = (board_size // 2, board_size // 2)

# Define the update function for the player position
def update_position(key):
    global player_pos
    if key == 'h':
        new_x = player_pos[0] - 1
        new_y = player_pos[1]
    elif key == 'n':
        new_x = player_pos[0] + 1
        new_y = player_pos[1]
    elif key == 'b':
        new_x = player_pos[0]
        new_y = player_pos[1] - 1
    elif key == 'm':
        new_x = player_pos[0]
        new_y = player_pos[1] + 1
    else:
        return
    if new_x >= 0 and new_x < board_size and new_y >= 0 and new_y < board_size:
        player_pos = (new_x, new_y)
        update_board()

# Define the update function for the board display
def update_board():
    plt.clf()
    plt.imshow(board, cmap='gray_r')
    plt.scatter(player_pos[1], player_pos[0], c='r', marker='o')
    plt.draw()

# Define the key press event for moving the player
def on_press(event):
    if event.key in ['h', 'n', 'm', 'b']:
        update_position(event.key)

# Set up the key press event listener
fig = plt.figure()
fig.canvas.mpl_connect('key_press_event', on_press)

# Initialize the board display
update_board()

# Show
plt.show()
