import random
ques=random.randint(1,100)
l1=['a','b']

def greater(x):
    print("the number is greater than", random.randint(ques-10,ques-1))

def smaller(x):
    print("the number is smaller than", random.randint(ques+1,ques+10))


while True:
    ans=int(input('enter your guess'))
    if ans==ques:
        print('You guessed correct')
        break
    else:
        hint=random.choice(l1)
        if hint=='a':
            greater(ques)
        if hint=='b':
            smaller(ques)
