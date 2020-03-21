import turtle


        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")

    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("red")
    brad.speed(20)
    for loop in range(0,36):
        brad.right(10)
        for i in range(1,4):
            brad.forward(100)
            brad.right(120)
    brad.right(90)
    brad.forward(200)
    window.exitonclick()

draw_art()
