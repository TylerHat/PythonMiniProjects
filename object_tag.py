import numpy as np
import matplotlib.pyplot as plt

# Set up the game board
board_size = 20
board = np.zeros((board_size, board_size))
player_pos = (board_size // 2, board_size // 2)
score = 0
# Spawn an object randomly on the board
object_pos_1 = (np.random.randint(0, board_size), np.random.randint(0, board_size))
object_pos_2 = (np.random.randint(0, board_size), np.random.randint(0, board_size))


def update_position(key):
    global player_pos
    global board
    global object_pos_1
    global object_pos_2
    global score
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
      
        if (new_x, new_y) == object_pos_1:
            board[new_x, new_y] = 1
            object_pos_1 = (np.random.randint(0, board_size), np.random.randint(0, board_size))
            score += 1
        elif (new_x, new_y) == object_pos_2:
            board[new_x, new_y] = 1
            object_pos_2 = (np.random.randint(0, board_size), np.random.randint(0, board_size))
            score += 1 
        else:
            player_pos = (new_x, new_y)
            update_board()



def update_board():
    plt.clf()
    plt.imshow(board, cmap='gray_r')
    plt.scatter(player_pos[1], player_pos[0], c='r', marker='o')
    plt.scatter(object_pos_1[1], object_pos_1[0], c='g', marker='s')
    plt.scatter(object_pos_2[1], object_pos_2[0], c='g', marker='s')

    plt.draw()

# Define the key press event for moving the player
def on_press(event):
    if event.key in ['h', 'n', 'm', 'b']:
        update_position(event.key)

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
ax.text(5, 10.5, f"Value: {score}", ha='center')
fig.canvas.mpl_connect('key_press_event', on_press)

update_board()


plt.show()
print("Your score was: "+ str(score))
