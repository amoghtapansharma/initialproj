# Conway's way of life.
import copy, time, random
height = 20
width = 60

#Create a list of list for the cells:
nextcells = []
for y in range(height):
     column = []
     for x in range(width):
         if random.randint(0, 1) == 0:
             column.append('#') #Adds a living cell.
         else:
             column.append(' ') #Adds a dead cell.
     nextcells.append(column) # Nextcells becomes a list of lists.

while True: # Main program loop.
     print('\n\n\n\n\n') #Separates each step by empty lines.
     currentcells = copy.deepcopy(nextcells)

     #Print currentcellson the screen
     for y in range(height):
         print()
         for x in range(width):
             print(currentcells[y][x], end='') #print # or space.

     #Calculate the next step's cells based on current step's cells:
     for y in range(height):
         for x in range(width):
             #Get neighbouring cell's co-ordinates:
             neighbors = [
                (y-1, x-1), (y-1, x), (y-1, x+1),
                (y, x-1),             (y, x+1),
                (y+1, x-1), (y+1, x), (y+1, x+1)
             ]

             #Checking which cell is alive:
             num = 0
             for ny, nx in neighbors:
                if 0 <= ny < height and 0 <= nx < width:
                    if currentcells[ny][nx] == '#':
                        num += 1

             #Making a cell alive or dead, based on rules.
             if currentcells[y][x] == '#' and (num == 2 or num == 3) :
                 nextcells[y][x] = '#'
             elif currentcells[y][x] == ' ' and num == 3:
                 nextcells[y][x] = '#'
             else:
                 nextcells[y][x] = ' '
     time.sleep(1)

