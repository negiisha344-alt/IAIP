import tkinter as tk
import random

# Game settings
width = 600
height = 400
size = 20
speed = 100

score = 0
direction = "right"

# Create window
root = tk.Tk()
root.title("Snake Game")

canvas = tk.Canvas(root, width=width, height=height, bg="black")
canvas.pack()

score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
score_label.pack()

# Starting position of snake
snake = [
    [300, 200],
    [280, 200],
    [260, 200]
]

food = [0, 0]


def make_food():
    food[0] = random.randrange(0, width, size)
    food[1] = random.randrange(0, height, size)


def change_direction(new_direction):
    global direction

    if new_direction == "up" and direction != "down":
        direction = "up"
    elif new_direction == "down" and direction != "up":
        direction = "down"
    elif new_direction == "left" and direction != "right":
        direction = "left"
    elif new_direction == "right" and direction != "left":
        direction = "right"


def move_snake():
    global score

    x = snake[0][0]
    y = snake[0][1]

    if direction == "up":
        y -= size
    elif direction == "down":
        y += size
    elif direction == "left":
        x -= size
    elif direction == "right":
        x += size

    new_head = [x, y]
    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        score_label.config(text="Score: " + str(score))
        make_food()
    else:
        snake.pop()


def game_over():
    canvas.create_text(
        width // 2,
        height // 2,
        text="Game Over!",
        fill="white",
        font=("Arial", 30)
    )


def game():
    move_snake()

    head = snake[0]

    # Check wall collision
    if head[0] < 0 or head[0] >= width or head[1] < 0 or head[1] >= height:
        game_over()
        return

    # Check collision with itself
    if head in snake[1:]:
        game_over()
        return

    canvas.delete("all")

    # Draw snake
    for part in snake:
        canvas.create_rectangle(
            part[0],
            part[1],
            part[0] + size,
            part[1] + size,
            fill="green"
        )

    # Draw food
    canvas.create_oval(
        food[0],
        food[1],
        food[0] + size,
        food[1] + size,
        fill="red"
    )

    root.after(speed, game)


# Keyboard controls
root.bind("<Up>", lambda event: change_direction("up"))
root.bind("<Down>", lambda event: change_direction("down"))
root.bind("<Left>", lambda event: change_direction("left"))
root.bind("<Right>", lambda event: change_direction("right"))

make_food()
game()

root.mainloop()
