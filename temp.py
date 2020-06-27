import turtle

t = turtle.Turtle()


def static_part():
    t.penup()
    t.goto(-320, 250)
    t.pendown()
    t.color('blue')
    turtle.bgcolor("yellow")
    style1 = ('Courier', 20, 'italic')
    t.write('Guess the word: ', font=style1, align='left')
    t.hideturtle()

    t.penup()
    t.goto(-320, -150)
    t.pendown()
    t.color('green')
    t.write('Wrong guesses : ', font=style1, align='left')
    t.hideturtle()


def word(w1):
    t.penup()
    t.goto(-320, 220)
    t.pendown()
    t.color('blue')
    style1 = ('Courier', 22, 'italic')
    t.write(w1, font=style1, align='left')
    t.hideturtle()


def wrong(w2):
    t.penup()
    t.goto(-320, -200)
    t.pendown()
    t.color('green')
    style1 = ('Courier', 20, 'italic')
    t.write(w2, font=style1, align='left')
    t.hideturtle()


def attempt(n):
    n = str(n)
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.color('black')
    style1 = ('Courier', 18, 'italic')
    t.write('Yow have ' + n + ' attempts left', font=style1, align='center')
    t.hideturtle()


def part_plus():
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.begin_fill()
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.end_fill()


def part_1():
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.color('blue')
    t.dot(50)
    t.pensize(3)
    t.bk(50)
    t.lt(90)
    t.fd(80)
    t.rt(90)
    t.fd(60)
    t.pen(pencolor='blue', fillcolor='red')
    t.begin_fill()
    # t.color('red')
    t.fd(15)
    t.lt(90)
    t.fd(8)
    t.lt(90)
    t.fd(15)
    t.lt(90)
    t.fd(8)
    t.end_fill()


def part_2():
    # t.lt(90)
    # part_1()
    t.pen(pencolor='red', fillcolor='red')
    t.penup()
    t.fd(10)
    t.pendown()
    t.begin_fill()
    t.fd(8)
    t.rt(90)
    t.fd(8)
    t.lt(90)
    t.fd(15)
    t.lt(90)
    t.fd(8)
    t.rt(90)
    t.fd(8)
    t.lt(90)
    t.fd(15)
    t.lt(90)
    t.fd(8)
    t.rt(90)
    t.fd(8)
    t.lt(90)
    t.fd(15)
    t.lt(90)
    t.fd(8)
    t.rt(90)
    t.fd(8)
    t.lt(90)
    t.fd(15)
    t.end_fill()





w = "****"
w3 = "asbsjb"
n1 = 8
static_part()
word(w)
wrong(w3)
attempt(n1)
part_1()
part_2()
turtle.done()
