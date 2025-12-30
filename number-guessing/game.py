import random
print('Welcome to the Number Guessing Game!')
print('lessgooooo')
name = input('What is your name?')
print('Hello', name)
print('---------------------------------------------------------------------------')

secret_number = random.randint(1, 20)
attempts = 0
high_hints = ['woahh! Reaching for the clouds!! huhh?!', 'Too high...maybe', 'oops, over the rainbow!!']
low_hints = ['thats under the radar!!', 'too low...aim higher', 'lower than your height!']
score = 200
while True:
 attempts += 1
 guess = int(input('Guess a number between 1 and 20: '))
 print('----------------------------------------------------------')
 if guess > secret_number:
  print(random.choice(high_hints))
  score -= 10
  print('SCORE: ', score)
  print('----------------------------------------------------')
 elif guess < secret_number:
    print(random.choice(low_hints))
    score -= 10
    print('SCORE: ', score)
    print('-----------------------------------------------------')
 else:
  print('You GOt it!!!')
  break
print('ATTEMPTS: ', attempts)
print('FINAL SCORE: ', score)
