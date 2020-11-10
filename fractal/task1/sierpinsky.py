import tkinter as tk
import turtle
import math
import time

it = 0
temp = 0
points = {}
n=0

def main():
    root, t = initialize_window()

def initialize_window():
    # creates main window
    root = tk.Tk()
    root.title('Sierpinsky triangle')
    root.configure(bg='lightgrey')
    root.configure(width=1100, height=700)

    # centers main windows
    winWidth = root.winfo_reqwidth()
    winwHeight = root.winfo_reqheight()
    posRight = int(root.winfo_screenwidth() / 2 - winWidth / 2)
    posDown = int(root.winfo_screenheight() / 2 - winwHeight / 2)
    root.geometry('+{}+{}'.format(posRight, posDown))

    # creates drawing canvas
    canvas = tk.Canvas(master = root, width = 700, height = 700, bg="white")
    canvas.pack_configure(side='left')
    screen = turtle.TurtleScreen(canvas)

    # turtle init
    t = turtle.RawTurtle(screen)
    t.hideturtle()
    t.shape("circle")
    t.shapesize(0.3,0.3,0.7)
    screen.tracer(False)

    # creates iterartion label
    it_str = tk.StringVar(root,'0','iteration')
    it_num= tk.Label(root, textvariable=it_str, font=("Helvetica", 16))
    label = tk.Label(root,text='iteration:', font=("Helvetica", 16))
    label.pack()
    it_num.pack()

    # for entering point codes
    code = tk.StringVar(root, '0', 'code')
    code_entry = tk.Entry(root, font=("Helvetica", 16), textvariable=code)
    code_entry.insert(0, "enter quaternary code:")
    code_entry.pack_configure(side="bottom")

    #
    xy = tk.StringVar(root, 'x:y', 'xy')
    coords = tk.Message(root, width=400, font=("Helvetica", 16), textvariable=xy)
    coords.pack_configure(side="bottom")

    # button init
    enter_code = tk.Button(root, text="find", font=("Helvetica", 16),
                           command=lambda x1=t, x2=code, x3=root, x4=xy:
                           find_code(x1, x2, x3, x4))
    enter_code.pack_configure(side="bottom")

    # reacts to Enter presses and iterates
    canvas.bind('<Return>',
                lambda event, x1=it_str, x2=root, x3=t:
                iterate(event, x1, x2, x3))
    canvas.bind('<Button-1>', lambda event, x1=canvas, x2=root, x3=code, x4=t, x5=xy:
                callback(event, x1, x2, x3, x4, x5))
    canvas.focus_force()
    canvas.pack()


    screen.update()
    screen.mainloop()

    return root, t

def callback(event, canvas, root, code, t, coords):
    x = (event.x - 350) * (1.0)
    y = (event.y - 350) * (-1.0)
    d = {}
    for key, value in points.items():
        d.update({key:math.sqrt(math.pow(x-value[0],2)
                           + math.pow(y-value[1],2))})

    min_distance = [key for key in d if d[key] == min(d.values())]

    if d.get(min_distance[0]) < 10:
        code.set(str(min_distance[0]))
        find_code(t, code, root, coords)


def iterate(event, it_str, root, t):
    global it
    it += 1
    it_str.set(str(it))
    sierpinski(t)
    root.update()

# find point in triangle by code and highlights it
def find_code(t, code, root, coords):
    global temp
    t.clearstamp(temp)
    tmp = str(code.get())
    x, y = points.get(tmp)
    tmp = '(' + str(round(x,3)) + " : " + str(round(y,3)) + ")"
    coords.set(tmp)
    root.update()

    t.penup()
    t.color("red", "red")
    t.setpos(x,y)
    t.pendown()

    temp = t.stamp()
    t.color('white','white')

# main fractal creation function
def sierpinski(t):
    side = 700
    newside = side / math.pow(2,it-2)
    newside1 = side / math.pow(2,it-1)

    global temp

    if it == 1:
        t.color('black','black')
        draw(t, 0, 310, side, create=False)
    elif it == 2:
        t.color('white','white')
        draw(t, 0, -(side*math.cos(math.pi/6))+310, newside1, True)
    elif it > 2:
        tmp = temp
        temp = len(points)
        points1 = points.copy()

        for i in range(tmp, len(points), 3):
            points1.popitem()
            points1.popitem()
            x, y = points.get(points1.popitem()[0])

            # up and draw
            draw(t, x, y+(newside*math.cos(math.pi/6)), newside1, True)

            # back at start, left and draw
            jump(t, x, y)
            draw(t, x-(newside/2), y, newside1, True)

            # back at start, right and draw
            jump(t, x, y)
            draw(t, x+newside/2, y, newside1, True)

def draw(t, x, y, side, invert=False, create=True):
        global n
        t.setheading(0)
        if invert:
            inv = -1
        else:
            inv = 1

        jump(t, x, y)
        if create:
            n += 1
            if n % 4 == 0:
                n += 1
            points.update({create_tag(n):[round(t.xcor(), 4), round(t.ycor(), 4)]})
        t.begin_fill()
        t.left(-120*inv)
        t.forward(side)
        for k in range (2):
            if create:
                n += 1
                if n % 4 == 0:
                    n += 1
                points.update({create_tag(n):[round(t.xcor(), 4), round(t.ycor(), 4)]})
            t.left(120*inv)
            t.forward(side)
        t.end_fill()

def jump(t, x, y):
    t.penup()
    t.setpos(x,y)
    t.pendown()

def create_tag(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 4)
        nums.append(str(r))
    return ''.join(reversed(nums))

main()
