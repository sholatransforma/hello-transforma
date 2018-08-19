#program guessing a number and to know if you are close or far from the number you guessed.
a = 65
guess = int(input('enter your guess'))
if (guess == a):
    print('you are correct')
if (a - guess < 10):
    print('you are close')
else:
    print('you are far')
