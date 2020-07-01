from .turtle_part import turtle_part



static_part()
turns = 8  # this is the total number of turns
attempt(turns)  # Prints available number of turns in turtle screen


print("**************************   PLAYER 1   **************************")
print(" ( MAKE SURE PLAYER 2 IS NOT PEAKING ! ) ")
word = input("ENTER YOUR WORD  ( IF IT HAS A SPACE, USE '-', E.G. ICE-CREAM ) :")  # enter the actual word
hint = input(" PLEASE GIVE A HINT : ")  # enter some hint

clearsc()


print("**************************   PLAYER 2   **************************")
print("HINT: " + hint)


# function to get all occurance of a character


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

wordfn(guessed_word)

while turns > 0:

    # guessed word completely matches with the word then break and print win
    if guessed_word == word:
        print("You Win")
        won()
        break

    # check if the user has any turn left
    guess = input("guess a character:")

    if guess not in word:
        turns -= 1
        attempt(turns)
        guesses += guess
        wrong(guesses)
        draw(8 - turns)
        print("Wrong Guessed are : {}".format(guesses))
        print("You have", + turns, 'more guesses')
    else:
        allIndexes = list(charFind(word, guess))
        for ind in allIndexes:
            guessed_word = replace_str_index(guessed_word, ind, guess)
        print("Prediction so far : {}".format(guessed_word))
        wordfn(guessed_word)

# call the function to update the turtle screen on every iteration
# pass guessed_word
# pass wrong prediction
# pass a flag for right or wrong

if turns == 0:
    print("You Loose")
    lose()
