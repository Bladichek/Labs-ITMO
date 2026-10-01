import time
import sys
import os
BLUE = "\u001b[44m"
RED = "\u001b[41m"
WHITE = "\u001b[47m"
GREEN = "\u001b[42m"
YELLOW = "\u001b[43m"
RESET = "\u001b[0m"
ERASE = "\x1B[2K"
BEGIN = "\x1B[G"


def flag():
    pixel = '  '
    length = 30
    for color in [YELLOW, GREEN, RED]:
        for i in range(3):
            print(f'{color}{pixel*length}{RESET}')



def uzor():
    height = 20
    widht = 40
    pixel='  '
    while True:
        for color in [RED, GREEN, YELLOW, BLUE]:

            for i in range(height-1):
                offset = int((361 - (19 - i) ** 2) ** 0.5)
                print(WHITE+pixel*offset + color+pixel*2 + WHITE+pixel*(widht-2*offset-4) + color+pixel*2+ WHITE+pixel*offset+ RESET)
            print(f'\u001b[{height + 1}A')
            print(f'\u001b[{widht + 1}D')
            time.sleep(1)


def anim():
    states=[
        'A_____a',
        'a.____a',
        'a_.___a',
        'a__.__a',
        'a___._a',
        'a____.a',
        'a_____A',
        'a____.a',
        'a___._a',
        'a__.__a',
        'a_.___a',
        'a.____a',
    ]
    while True:
        for state in states:
            print(state)
            time.sleep(0.2)
            print("\u001b[H\u001b[J", end="") #на MacOs библиотека os не работет

def sequence():
    f=open('sequence.txt').readlines()
    ch=[]
    nch=[]
    for i in range(len(f)):
        if i%2==0: #нумерация с 0
            ch.append(abs(float(f[i])))
        else:
            nch.append(abs(float(f[i])))

    ch_avg = sum(ch)/len(ch)
    nch_avg = sum(nch)/len(nch)

    print(ch_avg, nch_avg)
    print(f'{BLUE}{" " * round(ch_avg*5)}{RESET} {ch_avg / (ch_avg+nch_avg) * 100}%')
    print(f'{RED}{" " * round(nch_avg*5)}{RESET} {nch_avg / (ch_avg+nch_avg) * 100}%')
#flag()
#uzor()
anim()
#sequence()