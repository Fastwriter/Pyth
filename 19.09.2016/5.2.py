import random
x=random.choice(['rock','paper','scissors'])
y=str(input('Your step, my friend:'))
if(x=='rock' and y=='scissors' or x=='paper' and y=='rock' or x=='scissors' and y=='paper'):
    print('Computer wins. Its answer was',x)
if(y=='rock' and x=='scissors' or y=='paper' and x=='rock' or y=='scissors' and x=='paper'):
    print('You win, DaNu) Computer`s answer was',x)
if(x=='rock' and y=='rock' or x=='paper' and y=='paper' or x=='scissors' and y=='scissors'):
    print('DRAW...')
