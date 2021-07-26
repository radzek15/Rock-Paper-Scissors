import random

options = ['rock', 'paper', 'scissors']

Massages = ['You win', 'You Lose', 'It is a tie']

cp_choice = random.choice(options)
choice = input('Please choose one of {}'.format(options))

results = {'rock':{
        'rock': Massages[2],
        'paper': Massages[0],
        'scissors': Massages[1]},
    'paper' : {
        "rock": Massages[1],
        "paper": Massages[2], 
        "scissors": Massages[0]},
    "scissors":{
        "rock": Massages[0],
        "paper": Massages[1],
        "scissors": Massages[2]}}

try:
    Winner = results[cp_choice][choice]
    print('Computer choose {}'.format(cp_choice))
    print(Winner)
except KeyError:
    print('You choose wrong, Please try again')