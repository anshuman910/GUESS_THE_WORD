import turtle


def script():
    s = turtle.Screen()
    s.bgcolor("yellow")
    s.title("GUESS THE WORD GAME")

    t = turtle.Turtle()
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t3 = turtle.Turtle()
    t4 = turtle.Turtle()

    def static_part():  # draws the static parts
        t4.ht()
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

    def wordfn(w1):  # draws the original word part
        t1.clear()
        t1.penup()
        t1.goto(-320, 220)
        t1.pendown()
        t1.color('blue')
        style1 = ('Courier', 22, 'italic')
        t1.write(w1, font=style1, align='left')
        t1.hideturtle()

    def wrong(w2):  # draws the wrong choises part
        t2.clear()
        t2.penup()
        t2.goto(-320, -200)
        t2.pendown()
        t2.color('green')
        style1 = ('Courier', 20, 'italic')
        t2.write(w2, font=style1, align='left')
        t2.hideturtle()

    def attempt(n):  # draws the remaining attempt part
        t3.clear()
        n = str(n)
        t3.penup()
        t3.goto(0, -250)
        t3.pendown()
        t3.color('black')
        style1 = ('Courier', 18, 'italic')
        t3.write('Yow have ' + n + ' attempts left', font=style1, align='center')
        t3.hideturtle()

    def part_1():  # draws the 1st part of ambulance
        t.fillcolor('white')
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
        t.fd(15)
        t.lt(90)
        t.fd(8)
        t.lt(90)
        t.fd(15)
        t.lt(90)
        t.fd(8)
        t.end_fill()

    def part_2():  # draws the 2nd part of ambulance
        t.pencolor('red')
        t.fillcolor('red')
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

    def part_3():  # draws the 3rd part of ambulance
        t.penup()
        t.rt(90)
        t.fd(10)
        t.pencolor('blue')
        t.pendown()
        t.rt(90)
        t.fd(55)
        t.rt(90)
        t.fd(18)
        t.lt(90)
        t.fd(55)

    def part_4():  # draws the 4th part of ambulance
        t.rt(90)
        t.fd(62)

    def part_5():  # draws the 5th part of ambulance
        t.rt(90)
        t.fd(44)
        t.dot(50)

    def part_6():  # draws the 6th part of ambulance
        t.fd(76)
        t.bk(65)

    def part_7():  # draws the 7th part of ambulance
        t.pensize(1)
        t.rt(90)
        t.fd(62)

    def part_8():  # draws the 8th part of ambulance
        t.pensize(3)
        t.penup()
        t.bk(8)
        t.rt(90)
        t.fd(8)
        t.pendown()
        t.fillcolor('white')
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

    def lose():  # DRAWS "YOU LOSE!"
        t.penup()
        t.goto(0, 150)
        t.pendown()
        t.pensize(5)
        t.pencolor('black')
        style1 = ('Courier', 25, 'italic')
        t.write('YOU LOSE!', font=style1, align='center')
        t.hideturtle()

    def won():  # DRAWS "YOU WON!"
        t.penup()
        t.goto(0, 150)
        t.pendown()
        t.pensize(5)
        t.pencolor('green')
        style1 = ('Courier', 25, 'italic')
        t.write('YOU WON!', font=style1, align='center')
        t.hideturtle()

    def draw(argument):  # switch for the ambulance drawing
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

    def clearsc():  # function to clear python shell screen
        print('\n' * 200)

    static_part()  # draws the static part
    turns = 8  # this is the total number of turns
    attempt(turns)  # Prints available number of turns in turtle screen

    print("**************************   PLAYER 1   **************************")
    print(" ( MAKE SURE PLAYER 2 IS NOT PEAKING ! ) ")
    word = input("ENTER YOUR WORD  ( IF IT HAS A SPACE, USE '-', E.G. ICE-CREAM ) :")  # enter the actual word
    hint = input(" PLEASE GIVE A HINT : ")  # enter some hint

    clearsc()  # clears the python shell screen

    print("**************************   PLAYER 2   **************************")
    print("HINT: " + hint)  # give the hint

    # function to get all occurrence of a character

    def charFind(str, ch):
        for i, ltr in enumerate(str):
            if ltr == ch:
                yield i

    # function to replace a character from the word
    def replace_str_index(text, index=0, replacement=''):
        return '%s%s%s' % (text[:index], replacement, text[index + 1:])

    # logs all wrong guess
    guesses = ''

    # the initial guessed word should be in form ***** with * the no. of time as that of length of word
    guessed_word = '*' * len(word)

    wordfn(guessed_word)  # draws the original word (initially filled with *)

    while turns > 0:

        # guessed word completely matches with the word then break and print win
        if guessed_word == word:
            print("You Win")
            won()  # draw "YOU WON!"


            restart = input(
                "Would you like to restart this program? ")  # asks if the user wants to restart the game or not
            if restart == "yes" or restart == "y":
                t.clear()
                t1.clear()
                t2.clear()
                t3.clear()
                t4.clear()
                script()
            if restart == "n" or restart == "no":
                print("Game is terminating. Goodbye.")
            break

        # check if the user has any turn left
        guess = input("guess a character:")

        if guess not in word:
            turns -= 1
            attempt(turns)  # DRAW THE ATTEMPTS REMAINING (UPDATED WITH LOOP)
            guesses += guess
            wrong(guesses)  # DRAWS THE WRONGLY GUESSED LETTERS
            draw(8 - turns)  # DRAW THE AMBULANCE PART BY PART
            print("Wrong Guessed are : {}".format(guesses))
            print("You have", + turns, 'more guesses')
        else:
            allIndexes = list(charFind(word, guess))
            for ind in allIndexes:
                guessed_word = replace_str_index(guessed_word, ind, guess)
            print("Prediction so far : {}".format(guessed_word))
            wordfn(guessed_word)  # DRAW THE ORIGINAL WORD WITH STARS REPLACED WITH CORRECT CHOICES

    # call the function to update the turtle screen on every iteration
    # pass guessed_word
    # pass wrong prediction
    # pass a flag for right or wrong

    if turns == 0:
        print("You Loose")
        lose()  # DRAWS  "YOU LOSE!"

        restart = input("Would you like to restart this program? ")  # asks if the user wants to restart the game or not
        if restart == "yes" or restart == "y":
            t.clear()
            t1.clear()
            t2.clear()
            t3.clear()
            t4.clear()
            script()
        if restart == "n" or restart == "no":
            print("Game is terminating. Goodbye.")






script()
turtle.done()  # TURTLE SCREEN IS DONE