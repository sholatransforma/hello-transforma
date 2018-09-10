#Create a program that will play the “dogs and cats” game with the user. 

import random

def compare_numbers(number, guess):
    
#dogs followed by cats
    homepets = [0,0]
    for x in range(number):
        if number[x] == guess[x]:
            homepets[1] += 1
        else:
            homepets[0] += 1
    return homepets

#to play the game
if __name__ == '__main__':
    play = True
    
#random of 4 digit number
    number = (random.randint (0,9999))
    guesses = 0

#explanation
    print('lets play the game of homepets')
    print('i will generate a number and you have to guess the numbers one digit at a time')
    print('for every number in the wrong place, you get a cat. For every one in the right place you get a dog.')
    print('the game ends when you get 4 cats')
    print('type exit at any prompt to exit')

    while play:
        guess = input('give your guess')
        if guess == 'exit':
            break
        homepetscount = compare_numbers(number, guess)
        guesses += 1

        print('you have' + str(homepetscount[0]) + 'dogs' + str(homepetscount[1]) + 'cats')

        if homepetscount[1] == 4:
            play = False
            print('you win the game after ' + str(guesses) + 'the number was' + str(number))
            break
        else:
            print('you are not right, try again')
        
              
