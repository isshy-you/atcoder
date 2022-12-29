# -*- coding: utf-8 -*-
# pip install requests
# pip install bs4
import requests
from bs4 import BeautifulSoup
import sys
import subprocess

args = sys.argv

if len(args) >= 3 :
    abc = args[1]
    problem = args[2]
    URL = 'https://atcoder.jp/contests/abc'+str(args[1]+'/tasks/abc'+str(args[1])+'_'+args[2])
    if len(args) >= 4 :
        select = int(args[3])
    else:
        select = 0
else:
    print('\nUsage : py '+args[0]+' (abc_number) ([a|b|c|d|e|f|g])\n')
    exit()
# URL = 'https://atcoder.jp/contests/abc282/tasks/abc282_c'
res = requests.get(URL)
soup = BeautifulSoup(res.text,"html.parser")
pre = soup.select('span.lang-ja div.part pre')
flag = True
cnt = 1
for ii,jj in enumerate(pre):
    if jj.string != None :
        if (select == 0 or cnt == select) :
            if flag : 
                with open("input{}.txt".format(cnt), mode="w") as f:
                    f.write(jj.string.replace('\r',''))
                if len(args) < 5:
                    print('<<< input-{} <<<'.format(cnt))
                    print(jj.string)
            else : 
                with open("output{}.txt".format(cnt), mode="w") as f:
                    f.write(jj.string.replace('\r',''))
                if len(args) < 5 :
                    print('>>> output-{} >>>'.format(cnt))
                    print(jj.string)
                else :
                    print('=== output/answer-{} ==='.format(cnt))
                    print(jj.string[:-1])
                    # command prompt
                    cmd = 'py ' + args[4] + ' < ' + 'input{}.txt'.format(cnt) + ' > ' + "answer{}.txt".format(cnt)
                    # PowerShell
                    # Get-Content input.txt | python .\hogehoge.py
                    subprocess.run(cmd, shell=True)
                    with open("answer{}.txt".format(cnt), mode="r") as f:
                        print(f.read()[:-1])
        if not flag :
            cnt = cnt + 1
        flag = not flag


    