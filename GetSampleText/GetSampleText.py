# -*- coding: utf-8 -*-
# pip install requests
# pip install bs4
import requests
from bs4 import BeautifulSoup
import sys
import subprocess

args = sys.argv

if len(args) >= 3 :
    contest = str(args[1])
    num = str(args[2])
    problem = str(args[3])
    URL = 'https://atcoder.jp/contests/'+contest+num+'/tasks/'+contest+num+'_'+problem
    # print(URL)
    # URL = 'https://atcoder.jp/contests/abc282/tasks/abc282_c'
    # URL = 'https://atcoder.jp/contests/arc153/tasks/abc153_b'
    if len(args) >= 5 :
        select = int(args[4])
    else:
        select = 0
else:
    print('\nUsage : py '+args[0]+' [abc|arc] (number) ([a|b|c|d|e|f|g]) (sample_number) (code.py)\n')
    exit()
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
                    cmd = 'py ' + args[5] + ' < ' + 'input{}.txt'.format(cnt) + ' > ' + "answer{}.txt".format(cnt)
                    # PowerShell
                    # Get-Content input.txt | python .\hogehoge.py
                    subprocess.run(cmd, shell=True)
                    with open("answer{}.txt".format(cnt), mode="r") as f:
                        print(f.read()[:-1])
        if not flag :
            cnt = cnt + 1
        flag = not flag


    