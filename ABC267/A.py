# -*- coding: utf-8 -*-
# A
DEBUG=False
# DEBUG=True

S = input()

if DEBUG : print('INPUT = ',S)

week = {'Monday':5,\
        'Tuesday':4,\
        'Wednesday':3,\
        'Thursday':2,\
        'Friday':1\
        }

print(week[S])

