print('This is a Tic-Tac-Toe game for 2 players.')
print('Player one will play first, then Player two.')

grid = []
#For printing what's is inside the grid.
for y  in range(5):
    column = []
    if y % 2 == 0:
        for x in range(5):
            if x % 2 == 0:
                column.append(' ')
            else:
                column.append('|')
    else:
        for x in range(5):
            if x % 2 == 0:
                column.append('-')
            else:
                column.append('+')
    grid.append(column)

#For adding values to the grid.
s = (0, 2, 4)
for y in s:
    for x in s:
        grid[y][x] = int((x/2) + 2 + 3*((y/2) + 2)) -7

inside = {}
#For adding items in 'inside' dictionary.
for y in s:
    for x in s:
        num = 'grid['+ str(y) + '][' + str(x) + ']'
        inside.setdefault(grid[y][x], num)

# Function for printing the grid.
def print_grid():
    for a in range(5):
        for b in range(5):
            print(grid[a][b], end='')
        print()

print_grid()

print('From the numbers in the grid please select which place would you play your turn.')

#Forming the loop for the main game. (This runs 9 times.)
turn = 'X'
print('Turn is of ' + turn)

for t in range(9):

    #Taking in the input.
    giyan = int(input())
    if giyan in inside.keys():
        value = inside[giyan]

        # Extracting coordinates from the string
        position = value.strip('grid[]').split('][')
        y, x = int(position[0]), int(position[1])
        grid[y][x] = turn

        print_grid()

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
        print('Now the turn is of ' + turn)

    else:
        print('Please enter a correct input.')
    
print('Thank you for playing.')