import turtle

t = turtle.Turtle()
t1 = turtle.Turtle()
s= turtle.Screen()

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
    stars = ''
    n3 = len(w1)
    for n2 in range(n3):
        stars = stars + '  *'

    t.penup()
    t.goto(-320, 220)
    t.pendown()
    t.color('blue')
    style1 = ('Courier', 22, 'italic')
    t.write(stars, font=style1, align='left')
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
    t1.clear()
    n = str(n)
    t1.penup()
    t1.goto(0, -250)
    t1.pendown()
    t1.color('black')
    style1 = ('Courier', 18, 'italic')
    t1.write('Yow have ' + n + ' attempts left', font=style1, align='center')
    t1.hideturtle()


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
    t.pencolor('blue')
    t.fillcolor('red')
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


w = "****"
w3 = "asbsjb"
n1 = 8
static_part()
word(w)
wrong(w3)
for n in range(8):
    # s.update()
    attempt(n)
part_1()
#part_2()
#part_3()
#part_4()
#part_5()
#part_6()
#part_7()
#part_8()
#lose()
# won()
turtle.done()
