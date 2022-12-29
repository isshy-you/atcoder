
# 2次元配列の初期化
def init_2d_list(sizex,sizey,value):
    dat = [[value]*(sizex+1) for i in range(sizey+1)]
    if DEBUG : print('dat=',dat)
    if DEBUG : print('x y #')
    for xx in range(sizex):
        for yy in range(sizey):
            if DEBUG : print(xx,yy,dat[yy][xx])
    return(dat)

# 秒を時間・分表示
def print_time(seconds):
    minites = seconds // 60
    sec = seconds % 60

    hours = minites // 60
    min = minites % 60

    hour = hours % 60
    days = hours // 24
    print('{:d}sec = {:02d} days,{:02d} hours,{:02d} minites,{:02d} seconds'.format(seconds,days,hour,min,sec))

# リスト型標準入力
def input_list():
    dat = list(map(int,input().split()))
    return(dat)

# 2次元リスト型標準入力
def input_list_2d(x,y):
    dat=[]
    for yy in range(y):
        values = list(map(int,input().split()))
        # if len(values)==x:
        dat.append(values)
    return(dat)

# 再帰実行の制限
import sys
sys.setrecursionlimit(100000)

# DEUG定義
DEBUG=False
# DEBUG=True

# 使いそうな定義
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
digit = '0123456789'
hex = '0123456789ABCDEF'

### DEFの動作テスト・サンプル

dat=init_2d_list(2,4,0)

print_time(61)

print('alphabet[10]=',alphabet[10])

print('digit[1]=',digit[1])

print('カンマ区切りで複数数値入力')
dat = input_list()
print('入力後',dat)

print("input x(columns)=3,y(line)=2")
print('カンマ区切りで複数数値入力、複数行入力')
dat = input_list_2d(3,2)
print('入力後',dat)
dat.sort()
print('順ソート後=',dat)
dat.sort(reverse=True)
print('逆ソート後=',dat)

# リストの初期化
# dat = [[0]*(sizex+1) for i in range(sizey+1)]
# flag = [[0]*(N) for i in range(N)]

# 変数名と値を取得
# ls = [key for key in locals().keys()]
# ls = [key for key in globals().keys()]
