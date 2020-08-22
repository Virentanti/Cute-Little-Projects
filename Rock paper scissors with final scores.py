import random
l1=['ROCK', 'PAPER', 'SCISSORS']
c_point=0
u_point=0
t=int(input("Enter how many matches you wanna play"))
for i in range(t):
    u=str(input("enter your call ROCK, PAPER, SCISSORS!"))
    c=random.choice(l1)
    print(c)
    if u.upper()==c:
        print("You won!")
        u_point+=1
    else:
        print("Better luck next time")
        c_point+=1
print("final scores are computer {} and user {}".format(c_point,u_point))
