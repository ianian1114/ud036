import turtle


        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(8)
    for loop in range(0,36):
        brad.right(10)
        for i in range(1,5):
            brad.forward(100)
            brad.right(90)
    window.exitonclick()

draw_art()
