print('Let`s start the game...)')
p1=str(input('Your step(player1):'))
p2=str(input('Next, your step(player2):'))
if(p1=='rock' and p2=='scissors' or p1=='paper' and p2=='rock' or p1=='scissors' and p2=='paper'):
    print('Player1 wins')
if(p2=='rock' and p1=='scissors' or p2=='paper' and p1=='rock' or p2=='scissors' and p1=='paper'):
    print('Player2 wins')
if(p1=='rock' and p2=='rock' or p1=='paper' and p2=='paper' or p1=='scissors' and p2=='scissors'):
    print('DRAW...')
