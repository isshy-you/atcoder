# -*- coding: utf-8 -*-

def printYes():
    print('Yes')

def printNo():
    print('No')

# リスト型標準入力
def input_list():
    dat = list(map(int,input().split()))
    return(dat)



inp = input_list()
a = inp[0]
b = inp[1]

map = {1:[2,3],2:[4,5],3:[6,7],4:[8,9],5:[10,11],6:[12,13],7:[14,15],8:[],9:[],10:[],11:[],12:[],13:[],14:[],15:[]}

while(True):
    if b in map[a] or a in map[b]:
        printYes()
        exit()
    else:
        printNo()
        exit()
    
