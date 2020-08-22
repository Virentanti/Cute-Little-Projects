import random
l1=['ROCK', 'PAPER', 'SCISSORS']
while True:
    u=str(input("enter your call ROCK, PAPER, SCISSORS!"))
    c=random.choice(l1)
    print(c)
    if u.upper()==c:
        print("You won!")
    else:
        print("Better luck next time")
