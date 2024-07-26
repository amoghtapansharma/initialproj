import sys
def Comma_code():
    listA = []
    while True:
        num = input()
        listA.append(str(num))
        if num =='':
            print('Do you want to add an empty value to the string?')
            print('y/n')
            choice = input()
            if choice == 'y':
                continue
            else:
                listA.remove('')
        if num == 'q':
            listA.remove('q')
            break
    length = len(listA)-1
    for x in range(length):
        print(listA[x], end=', ')
    print(listA[length])

print('This is Comma Code. You can enter your value that can be added to a list.')
print('Press "q" when you complete your list.')
Comma_code()
print('Thank you.')
