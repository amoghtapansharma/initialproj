vov = ['a', 'e', 'i', 'o', 'u']

goa = input()
goa = goa.strip()
if goa.endswith('.'):
    gta = True
    goa = goa.strip('.')
    print(goa)
else:
    gta = False

if ' ' in goa:
    main = goa.split(' ')
else: 
     main = goa

if ' ' not in goa:
    pune = []
    for i, case in enumerate(main):
        if case.isupper():
            pune.append(i)
    if main[0].lower() in vov and main[0].isalpha():
        main = main + 'yay'
    elif main[0].isalpha():
        main = main[1:] + main[0] +'ay'
    main = main.lower()
    goa = []
    for x in main:
        goa.append(x)
    for f in pune:
        goa[f] = main[f].upper()
        goa =''.join(goa)
elif ' ' in goa:
    pink = []
    for words in main:
        coem = []
        if words[0].lower() in vov and words.isalpha():
            if words.isupper():
                if len(words) == 1:
                    word = words + 'yay'
                else:
                    word = words + 'YAY'
            else:
                word = words + 'yay'
        elif words.isalpha():
            if words.isupper():
                if len(words) == 1:
                    word = words + 'ay'
                else:
                    word = words[1:] + words[0] + 'AY'
            else:
                word = words[1:] + words[0] + 'ay'
        else:
            word = words
        for i, case in enumerate(words):
            if case.isupper():
                coem.append(i)
        if words.isupper():
            pink.append(word)
        else:
            goa = []
            for x in word.lower():
                goa.append(x)
            for f in coem:
                goa[f] = word[f].upper()
            pink.append(''.join(goa)) 
    goa = ' '.join(pink)

if gta:
    goa =goa + '.'
print(goa)