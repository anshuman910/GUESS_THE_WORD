import turtle

s = turtle.Screen()
s.bgcolor("yellow")
s.title("GUESS THE WORD GAME")

t = turtle.Turtle()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()


def static_part():
    t4.penup()
    t4.goto(-320, 250)
    t4.pendown()
    t4.color('blue')
    style1 = ('Courier', 20, 'italic')
    t4.write('Guess the word: ', font=style1, align='left')
    t4.hideturtle()
    t4.penup()
    t4.goto(-320, -150)
    t4.pendown()
    t4.color('green')
    t4.write('Wrong guesses : ', font=style1, align='left')
    t4.hideturtle()


def wordfn(w1):
    t1.clear()
    t1.penup()
    t1.goto(-320, 220)
    t1.pendown()
    t1.color('blue')
    style1 = ('Courier', 22, 'italic')
    t1.write(w1, font=style1, align='left')
    t1.hideturtle()


def wrong(w2):
    t2.clear()
    t2.penup()
    t2.goto(-320, -200)
    t2.pendown()
    t2.color('green')
    style1 = ('Courier', 20, 'italic')
    t2.write(w2, font=style1, align='left')
    t2.hideturtle()


def attempt(n):
    t3.clear()
    n = str(n)
    t3.penup()
    t3.goto(0, -250)
    t3.pendown()
    t3.color('black')
    style1 = ('Courier', 18, 'italic')
    t3.write('Yow have ' + n + ' attempts left', font=style1, align='center')
    t3.hideturtle()


def part_1():
    t.pen(fillcolor='white')
    t.begin_fill()
    t.penup()
    t.goto(-30, 0)
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


def part_3():
    t.penup()
    t.rt(90)
    t.fd(10)
    t.pen(pencolor='blue')
    t.pendown()
    t.rt(90)
    t.fd(55)
    t.rt(90)
    t.fd(18)
    t.lt(90)
    t.fd(55)


def part_4():
    t.rt(90)
    t.fd(62)


def part_5():
    t.rt(90)
    t.fd(44)
    t.dot(50)


def part_6():
    t.fd(76)
    t.bk(65)


def part_7():
    t.pensize(1)
    t.rt(90)
    t.fd(62)


def part_8():
    t.pensize(3)
    t.penup()
    t.bk(8)
    t.rt(90)
    t.fd(8)
    t.pendown()
    t.pen(fillcolor='white')
    t.begin_fill()
    t.fd(37)
    t.rt(90)
    t.fd(10)
    t.rt(90)
    t.fd(37)
    t.rt(90)
    t.fd(10)
    t.end_fill()
    t.end_fill()


def lose():
    t.penup()
    t.goto(0, 150)
    t.pendown()
    t.pensize(5)
    t.pen(pencolor='black')
    style1 = ('Courier', 25, 'italic')
    t.write('YOU LOSE!', font=style1, align='center')
    t.hideturtle()


def won():
    t.penup()
    t.goto(0, 150)
    t.pendown()
    t.pensize(5)
    t.pen(pencolor='green')
    style1 = ('Courier', 25, 'italic')
    t.write('YOU WON!', font=style1, align='center')
    t.hideturtle()


def draw(argument):
    switcher = {
        1: part_1,
        2: part_2,
        3: part_3,
        4: part_4,
        5: part_5,
        6: part_6,
        7: part_7,
        8: part_8

    }
    # Get the function from switcher dictionary
    func = switcher.get(argument)
    # Execute the function
    func()


def clearsc():
    print('\n' * 200)


turtle.done()
