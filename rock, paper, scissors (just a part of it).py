# Write your code here :-)
import random, sys
print('ROCK, PAPER, SCISSORS')
win=int(0)
lose=int(0)
tie=int(0)
state= (str(win)+' Wins, '+str(lose) +' Losses, '+str(tie)+' Ties')
print(state)
print('Enter your move: ROCK, PAPER, SCISSORS or QUIT')
while True:
    choose=input().upper()
    if choose=='QUIT':
        sys.exit()
    elif choose == 'ROCK' or choose == 'PAPER' or choose == 'SCISSORS':
        options = ('ROCK', 'PAPER', 'SCISSORS')
        cc=random.choice(options)
        print(cc)
        if cc==choose:
            tie=tie+1
        elif choose == 'ROCK':
             if cc == 'PAPER':
               lose= lose +1
             elif cc == 'SCISSORS':
                win = win +1
        elif choose == 'PAPER':
            if cc == 'ROCK':
                win += 1
            elif cc == 'SCISSORS':
                lose += 1
        elif choose == 'SCISSORS':
            if cc == 'ROCK':
                lose += 1
            elif cc == 'PAPER':
                win = win + 1
        state= (str(win)+' Wins, '+str(lose) +' Losses, '+str(tie)+' Ties')
        print(state)
    else:
        print('Only allowed input are Rock, Paper, Scissors or Quit.')
