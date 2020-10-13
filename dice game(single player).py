import random

player_money=1000
def game():
    global player_money
    guess=int(input('Enter your guess:'))
    if guess in range(1,7):
        if player_money>0:
            bet=int(input('How much you want to bet?'))
            if bet<=player_money:
                dice=random.randrange(1,6)
                if guess==dice:
                    print('Congratulations! You won')
                    player_money+=bet
                    print(f'Your money is {player_money}')
                    ans=str(input('press Y to play again or Press N to exit'))
                    if ans.upper()=='Y':
                        game()
                else:
                    print('Sorry! You lost')
                    player_money-=bet
                    print(f'Your money is {player_money}')
                    ans=str(input('press Y to play again or Press N to exit'))
                    if ans.upper()=='Y':
                        game()
            else:
                print('you dont have that kinda money \n Try again!')
                game()
        else:
            print('you have exausted your balance')
    else:
        print('Our dice doesnt have that kinda number \n Try again!')
        game()
game()
