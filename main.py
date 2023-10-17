from turtle import *
import random

# Set up the screen
win = Screen()
win.title("Game Tembak-Tembakan")
win.bgcolor("lightblue")
win.setup(width=600, height=600)
win.tracer(0)

# Create the player
player = Turtle()
player.shape("square")
player.color("red")
player.shapesize(stretch_wid=1, stretch_len=3)
player.penup()
player.goto(0, -250)

# Create a list to store bullets
bullets = []

# Create a list to store enemies
enemies = []

# Function to move the player left
def move_left():
    x = player.xcor()
    if x > -280:
        x -= 20
    player.setx(x)

# Function to move the player right
def move_right():
    x = player.xcor()
    if x < 280:
        x += 20
    player.setx(x)

# Function to shoot a bullet
def shoot():
    bullet = Turtle()
    bullet.shape("triangle")
    bullet.color("yellow")
    bullet.shapesize(stretch_wid=0.2, stretch_len=0.5)
    bullet.penup()
    bullet.goto(player.xcor(), player.ycor())
    bullets.append(bullet)

# Function to create an enemy
def create_enemy():
    enemy = Turtle()
    enemy.shape("circle")
    enemy.color("blue")
    enemy.penup()
    enemy.goto(random.randint(-290, 290), 290)
    enemies.append(enemy)

# Function for explosion effect
def explode(x, y):
    explosion = Turtle()
    explosion.hideturtle()
    explosion.shape("circle")
    explosion.color("red")
    explosion.shapesize(stretch_wid=3, stretch_len=3)
    explosion.penup()
    explosion.goto(x, y)
    explosion.showturtle()
    win.update()
    explosion.hideturtle()

# Keyboard bindings
win.listen()
win.onkeypress(move_left, "Left")
win.onkeypress(move_right, "Right")
win.onkeypress(shoot, "space")

# Function to move the bullets
def move_bullets():
    for bullet in bullets:
        y = bullet.ycor()
        y += 10
        bullet.sety(y)

# Function to move the enemies randomly
def move_enemies():
    for enemy in enemies:
        x = enemy.xcor()
        x += random.uniform(-1, 1)
        y = enemy.ycor()
        y -= 1
        enemy.setx(x)
        enemy.sety(y)

# Function to check for collisions
def check_collisions():
    for bullet in bullets:
        for enemy in enemies:
            if (
                (bullet.ycor() > enemy.ycor() - 10)
                and (enemy.xcor() - 10 < bullet.xcor() < enemy.xcor() + 10)
            ):
                bullet.hideturtle()
                bullets.remove(bullet)
                enemy.hideturtle()
                enemies.remove(enemy)
                explode(enemy.xcor(), enemy.ycor())  # Trigger explosion

# Main game loop
while True:
    win.update()

    # Move bullets
    move_bullets()

    # Move enemies
    move_enemies()

    # Create new enemies randomly
    if random.random() < 0.02:
        create_enemy()

    # Check for collisions
    check_collisions()

    # Check if enemy hits bottom
    for enemy in enemies:
        if enemy.ycor() < -290:
            enemy.hideturtle()
            enemies.remove(enemy)
