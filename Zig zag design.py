import time, sys
indent = 0
indentinc = True
try:
    while True:
        print(' '*indent +'*'*8)
        time.sleep(0.3)
        if indentinc:
            indent+=1
            if indent==4:
                indentinc=False

        elif indent:
            indent += -1
            if indent == 0:
                indentinc = True

except KeyboardInterrupt:
    sys.exit()
