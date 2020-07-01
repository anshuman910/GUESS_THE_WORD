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


def wordfn(w1):
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
    n = str(n)
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.color('black')
    style1 = ('Courier', 18, 'italic')
    t.write('Yow have ' + n + ' attempts left', font=style1, align='center')
    t.hideturtle()


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


def one():
    part_1()


def two():
    part_2()


def three():
    part_3()


def four():
    part_4()


def five():
    part_5()


def six():
    part_6()


def seven():
    part_7()


def eight():
    part_8()


def nine():
    lose()


def ten():
    won()


def draw(argument):
    switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine,
        10: ten,

    }
    # Get the function from switcher dictionary
    func = switcher.get(argument)
    # Execute the function
    func()


def clearsc():
    import os
    clear = lambda: os.system('cls')  # on Windows System
    clear()


while 1:

    print("**************************   PLAYER 1   **************************")
    print(" ( MAKE SURE PLAYER 2 IS NOT PEAKING ! ) ")
    word = input("ENTER YOUR WORD  ( IF IT HAS A SPACE, USE '-', E.G. ICE-CREAM ) :")  # enter the actual word
    hint = input(" PLEASE GIVE A HINT : ")  # enter some hint
    clearsc()

    guesses = ''
    g1 = ''

    turns = 8  # this is the total number of turns
    print("**************************   PLAYER 2   **************************")
    print("HINT: "+hint)

    while turns > 0:

        failed = 0  # counts the number of times a user fails

        # all characters from the input word taking one at a time.

        for char in word:

            # comparing that character with the character in guesses

            if char in guesses:
                print(char)

            else:
                print("_")

                # for every failure 1 will be incremented in failure

                failed += 1

        if failed == 0:
            # user will win the game if failure is 0  and 'You Win' will be given as output

            print("You Win")
            won()

            # this print the correct word
            print("The word is: ", word)
            break

        # if user has input the wrong alphabet then it will ask user to enter another alphabet

        guess = input("guess a character:")

        # every input character will be stored in guesses
        guesses += guess
        g1 = g1 + '  ' + guess

        # check input with the character in word
        if guess not in word:

            turns -= 1
            static_part()
            wordfn(word)
            wrong(g1)
            attempt(turns)

            # if the character doesn’t match the word  then “Wrong” will be given as output

            print("Wrong")

            # this will print the number of  turns left for the user

            print("You have", + turns, 'more guesses')

            if turns == 0:
                print("You Loose")
                lose()

turtle.done()
