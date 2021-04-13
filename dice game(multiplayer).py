import random

player1_money=1000
player2_money=1000

Player1= str(input('Player 1 Please enter your name '))
Player2= str(input('Player 2 Please enter your name '))

def money():
    print(f'{Player1} Your money is {player1_money}')
    print(f'{Player2} Your money is {player2_money}')

def p1_won():
    print(f'Congratulations {Player1}! You won')
    print(f'Sorry {Player2}! You lost')
    player1_money+=bet1
    player2_money-=bet2

def p2_won():
    print(f'Congratulations {Player2}! You won')
    print(f'Sorry {Player1}! You lost')
    player1_money-=bet1
    player2_money+=bet2

def Both_won():
    print(f'Congratulations {Player1} and {Player2}! You both won')
    player1_money+=bet1
    player2_money+=bet2

def nobody_won():
    print(f'Sorry {Player1} and {Player2}! You both lost')
    player1_money-=bet1
    player2_money-=bet2
def game():
    global player1_money, player2_money, Player1,Player2
    for i in range(5):
        guess1=int(input(f'{Player1} Enter your guess:'))
        guess2=int(input(f'{Player2} Enter your guess:'))
        if guess1 and guess2 in range(1,7):
            if player1_money>0 and player2_money>0:
                bet1=int(input(f'{Player1} How much you want to bet?'))
                bet2=int(input(f'{Player2} How much you want to bet?'))
                if bet1<=player1_money and bet2<=player2_money:
                    dice=random.randrange(1,6)
                    if guess1==dice and guess2!=dice:
                        p1_won()
                        money()
                    elif guess1!=dice and guess2==dice:
                        p2_won()
                        money()
                    elif guess1==dice and guess2==dice:
                        Both_won()
                        money()
                    else:
                        nobody_won()
                        money()
                else:
                    print('you dont have that kinda money \n Try again!')
                    game()
            else:
                print('you have exausted your balance')
        else:
            print('Our dice doesnt have that kinda number \n Try again!')
            game()
    if player1_money>player2_money:
        print(f'{Player1} Congratulations! You Won the game \n Your money is {player1_money}')
    else:
        print(f'{Player2} Congratulations! You Won the game \n Your money is {player2_money}')
game()
