#!/usr/bin/env python
# coding: utf-8

# In[21]:


def clearsc():
   print('\n' * 200)




print("**************************   PLAYER 1   **************************")
print(" ( MAKE SURE PLAYER 2 IS NOT PEAKING ! ) ")
word = input("ENTER YOUR WORD  ( IF IT HAS A SPACE, USE '-', E.G. ICE-CREAM ) :")  # enter the actual word
hint = input(" PLEASE GIVE A HINT : ")  # enter some hint


clearsc()

# In[22]:


turns = 8  # this is the total number of turns
print("**************************   PLAYER 2   **************************")
print("HINT: "+hint)


# In[23]:


#function to get all occurance of a character
def charFind(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield i


# In[24]:


#function to replace a character from the word
def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])


# In[26]:


#logs all wrong guess
guesses = ''

g1 = ''
#the initial guessed word should be in form ***** with * the no. of time as that of length of word
guessed_word='*'*len(word)

while turns > 0:
    
    #guessed word completly matches with the word then break and print win
    if(guessed_word==word):
        print("You Win")
        break
            
    #check if the user has any turn left            
    guess = input("guess a character:")

    if guess not in word:
        turns -= 1
        guesses += guess
        print("Wrong Guessed are : {}".format(guesses))
        print("You have", + turns, 'more guesses')
    else:
        allIndexes=list(charFind(word,guess))
        for ind in allIndexes:
            guessed_word=replace_str_index(guessed_word,ind,guess)
        print("Prediction so far : {}".format(guessed_word))

#call the function to update the turtle screen on every iteration
#pass guessed_word
#pass wrong prediction 
#pass a flag for right or wrong

if turns == 0:
    print("You Loose")


# In[7]:




