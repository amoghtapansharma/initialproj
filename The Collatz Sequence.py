def Collatz():
    global egg
    if int(egg) % 2 == 0:
        egg= int(egg)//2
    else:
        egg= int(egg)*3 + 1

print('Enter a number:', end='')
egg = input()
while egg != 1:
    Collatz()
    print(egg)
