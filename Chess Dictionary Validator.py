def isValidChessBoard(group):
    
    #For checking if all the pieces on the board are correct and in correct numbers.
    if len(group.get('wpawn', [])) == 8 and len(group.get('bpawn', [])) == 8:
        print('The board has all of its pawns and each have correct numbers of pawns.')
    
    pth2p = ['bishop', 'knight', 'rook']
    for x in pth2p:
        if len(group.get('w' + x, [])) == 2 and len(group.get('b' + x, [])) == 2:
            print('The board has all of its ' + x + ' and each have correct numbers of ' + x +'s.')

    pth1p = ['king', 'queen']
    for y in pth1p:
        if len(group.get('w' + y, [])) == 1 and len(group.get('w' + y, [])) == 1:
            print('The board has all of its ' + y + ' and each have correct numbers of ' + y +'s.')
        else:
            print('Here.')

    #Incoorect, not needing but was the first typed so keeping it here anywhay.
    sum = []
    for k,v in group.items():
        sum += v
    if len(sum) == 32:
        print('Good on numbers.')
    
    #Ensuring if all the pieces are on the board.
    #Makig a list of all possible destination on the chess board.
    giyan = [] 
    chan = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for a in range(8):
        for b in range(8):
            giyan.append(str(b + 1) + chan[a])
    giga = 0
    for s in range(32):
        if sum[s] in giyan:
            giga += 1
    #Still ensuring.
    if giga == 32:
        print('All the the pieces are on the chess board')
    else:
        print('Not all pieces are on the board.')
    
    #Making sure if none of the pieces overlap.
    gta = {}
    for a in sum:
        gta.setdefault(a, 0)
        gta[a] += 1
    pink = 0
    for a in gta.values():
        if a <= 1:
            pink += 1
    if pink == 32:
        print('All is good.')


import sys

ation = {'bking':['1e'], 'bqueen':['1d'], 'bbishop':['1c', '1f'], 
         'bknight':['1b', '1g'], 'brook':['1a', '1h'], 
         'bpawn':['2f', '2g', '2a', '2h', '2b', '2c', '2d', '2e'], 
         'wking':['8e'], 'wqueen':['8d'], 'wbishop':['8c', '8f'], 
         'wknight':['8b', '8g'], 'wrook':['8a', '8h'], 
         'wpawn':['7f', '7g', '7a', '7h', '7b', '7c', '7d', '7e']}

#The main code.
print('''This is Chess Dictionary Validator.
Please enter your chess board in the form of dictionary.
Black king as bking and white king as wking.
Same with all the other pieces.
Followed by their place on the board inside square brackets [].
      
Here is an example.
      ''')

print('Your Chess Board = ' + str(ation) +'\n')

print('Do you want to see it in action on the above chess board or do you want to enter your own chess board?')
print('y/n')
red = input()
if red == 'y':
    while True:
        print('Either enter your chess board or press "q" to quit.')
        man = input()
        if man == 'q':
            sys.exit()
        elif man != 'q' and len(man) == 1:
            print('Changed you mind.')
            isValidChessBoard(ation)
        else:
            isValidChessBoard(man)
elif red == 'n':
    isValidChessBoard(ation)
elif red != 'y' and red != 'n':
    print('Bro! It is a yes or no question.')