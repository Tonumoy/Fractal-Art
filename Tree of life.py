# Developer - Tonumoy Mukherjee


import turtle as tu


roo = tu.Turtle()  # Turtle object
wn = tu.Screen()  # Screen Object
wn.bgcolor("black")  # Screen background color
wn.title("Fractal Tree Pattern")
roo.left(90)  # moving the turtle 90 degrees towards left
# zero is the fastest speed. see https://docs.python.org/3/library/turtle.html#turtle.speed
roo.speed(0)


def draw_recursive(pensize: int, length: float, scale_factor: float, color: str) -> None:
    if (length < 10):
        return
    roo.pensize(pensize)  # Setting Pensize
    roo.pencolor(color)
    roo.forward(length)
    roo.left(30)  # moving the turtle 30 degrees towards left
    # drawing a fractal on the left of the turtle object 'roo' with a fraction of its length
    draw_recursive(pensize, length*scale_factor, scale_factor, color)
    roo.right(60)  # moving the turtle 60 degrees towards right
    # drawing a fractal on the left of the turtle object 'roo' with a fraction of its length
    draw_recursive(pensize, length*scale_factor, scale_factor, color)
    roo.left(30)  # moving the turtle 30 degrees towards left
    roo.pensize(pensize)
    roo.backward(length)  # returning the turtle back to its original psition


white = '#FFF8DC'
# parameters to make the same image
# (pensize, length, scale, color, turn function, turn amount)
tree_parameters = [
    (2, 20, 3.0/4.0, 'yellow', roo.right, 90),
    (2, 20, 3.0/4.0, 'magenta', roo.left, 270),
    (2, 20, 3.0/4.0, 'red', roo.right, 90),
    (2, 20, 3.0/4.0, white, roo.right, 0),
    (3, 40, 4.0/5.0, 'lightgreen', roo.right, 90),
    (3, 40, 4.0/5.0, 'red', roo.left, 270),
    (3, 40, 4.0/5.0, 'yellow', roo.right, 90),
    (3, 40, 4.0/5.0, white, roo.right, 0),
    (2, 60, 6.0/7.0, 'cyan', roo.right, 90),
    (2, 60, 6.0/7.0, 'yellow', roo.left, 270),
    (2, 60, 6.0/7.0, 'magenta', roo.right, 90),
    (2, 60, 6.0/7.0, white, roo.right, 90),
]


for changing_pen_size, changing_length, changing_scale, changing_color, turn_function, turn_amount in tree_parameters:

    draw_recursive(pensize=changing_pen_size,
                   length=changing_length,
                   scale_factor=changing_scale,
                   color=changing_color)

    # turn the turtle by some amount
    turn_function(turn_amount)


wn.exitonclick()
