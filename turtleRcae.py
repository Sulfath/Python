import turtle
import time
import random

HEIGHT, WIDTH = 800, 800
COLORS =['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']
  
def get_number_racers():
    racers =0
    while True:
        racers = input("Enter the number of races (2-10): ")
        if racers.isdigit():
            racers =int(racers)
        else:
            print("Invalid input. Try again!!")
            continue 

        if 2 <= racers <=10:
            return racers
        else:
            print("The number is not between 2 and 10. Try again !")   
    
def race(colors):
    turtles = create_Turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

        x, y = racer.pos()
        if y>= HEIGHT//2 - 10:
            return colors[turtles.index(racer)]

def init_turtle():
    TK_SILENCE_DEPRECATION=1
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title = 'Turtle Racing!!'
  
def create_Turtles(colors):
    Turtles = []
    spacingx = WIDTH // (len(colors)+1)
    for i,color in enumerate(colors):
        racer = turtle.Turtle()
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2+ (i+1)* spacingx,-HEIGHT//2 + 20)
        racer.pendown()
        racer.color(color)
        Turtles.append(racer)
    return Turtles
   
racers = get_number_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
winner=race(colors)
print("The winner is the turtle with color : ",winner)
time.sleep(5)



