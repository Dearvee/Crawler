import requests
from bs4 import BeautifulSoup
url1 = 'https://git.ahstu.cc/explore/users?page='
m = 9
users_name = []
for x in range(1,m):
    res1 = requests.get(url1+str(x))
    soup1 = BeautifulSoup(res1.text,'html.parser')
    for i in soup1.select('.item'):
        if len(i.select('.header a')) > 0:
            users_name.append(i.select('.header a')[0].text)
#get all user            
         
url2 = 'https://git.ahstu.cc/'
n = 4
#假设仓库数最多的用户不超过三页仓库
repositorys = []
for y in users_name:
    user_rep = 0
    print(y)
    for z in range(1,n):
        res2 = requests.get(url2+y+'?page='+str(z))
        soup2 = BeautifulSoup(res2.text,'html.parser')
        for i in soup2.select('.item'):
            if len(i.select('.name')) > 0:
                print('**********'+str(user_rep)+": "+i.select('.name')[0].text)
                user_rep = user_rep+1;
                repositorys.append(i.select('.name')[0].text)
    print('\n')
len(repositorys)


'''
git
**********0: MarkdownEditor_Node
**********1: CleanCodeOfJS
**********2: AcmEditor
**********3: Vim
**********4: NginxConf
**********5: guidetodatamining
**********6: Python-DHT
**********7: helper
**********8: SchoolVR
**********9: MiniUpload
**********10: AutoScript
**********11: BaiduShare
**********12: OJAssistant
**********13: Judge_client


acm


Tortoise


cuining


zj
**********0: cprogrammingII
**********1: JavaWeb
**********2: eq
**********3: CoreJava
**********4: ACMProgramming
**********5: cprogramming
**********6: Golang
**********7: AlgorithmDesign
**********8: blogs
**********9: python
**********10: GATspSolver
**********11: zjTools
**********12: OJDataMakerTools
**********13: math
**********14: AndroidProgramming
**********15: chess
**********16: learn


jiajl
**********0: attendance
**********1: attendancr


1881130216
**********0: jsp2
**********1: jsp


dyf
**********0: hehe


1881130..7
**********0: jsp


wangside
**********0: exam1


1881130206
**********0: jsp


1881130227


1881130333
**********0: jsp2
**********1: jsp


1884130103
**********0: jsp


ahkjxy_git
**********0: zm


dingweiqing
**********0: C
**********1: JSP


1884130111
**********0: KJS
**********1: jsp


1884130113
**********0: sama
**********1: tomo


1884130104
**********0: rui


1884130127
**********0: zyq


1884130219
**********0: TJ


1884130118
**********0: jsp
**********1: html
**********2: iindex
**********3: index


1884130124
**********0: html
**********1: sgs
**********2: jsp


heke
**********0: yuuka
**********1: tano


1884130116
**********0: lny
**********1: dd
**********2: ndd
**********3: jsp


1884130107
**********0: hhy


1884130105
**********0: nicaicai


1884130209


Ikaros


1884130109


1884130106
**********0: fhj


1884130117
**********0: shh


1884130123
**********0: ez


1884130119


1884130125


1884130218


1884130202


1884130210
**********0: ls1884130210
**********1: lsve


1884130225


1884130224
**********0: jsp1


1884130120
**********0: java


1884130212


1881130116
**********0: ahstugit
**********1: Ahstu_Libray


1881140207


Joker


bill


zhijzan
**********0: ACMProgramming
**********1: usaco-training
**********2: UG-Tower


wfy


Fan
**********0: AcmQuestions
**********1: JudgeOnline
**********2: helper
**********3: AndroidProgramming
**********4: AlgorithmDesign


1881130208


aoj-wzl


cdy


HK


LI
**********0: JAVACode


dearvee
**********0: Crawler
**********1: Web
**********2: Course
**********3: Android


hj


wzy
**********0: wzy


1881140224


corki
**********0: Android-notes
**********1: Java-class


canglingyue
**********0: demo


zhang0ZGC


byqs


malone_ding


txl


pmathticol
**********0: ajstu_oj_code


hzy767596742


CJ2701150103


LDQ
**********0: everyday
**********1: startMove
**********2: 1-webBuilding


88888888


vyoung
**********0: oj
**********1: php
**********2: shell
**********3: mywebproject


hanqianqian


sf


Jy


SMILE-TO-YOU


2701160208


geh
**********0: C_Course


zjq
**********0: AKOJ


1881130221


ContestSolution


Neo


PengrongDai


wangjun


2304150240


dazhi


lgb
**********0: acm


chshru
**********0: acm


2604150210


ZTZ


2703150231


forging


dfy123


694995658


Jarvis
**********0: Webs
**********1: Web
**********2: Android


jal


17375365520


songchaochen


fire


liuyanyan


zly


winer


tang


chzu2016211786


wangqiqi


ac_loser


echo


JK


weixiaobi


1887140107


1887140232


1887140141


China_Good_Code
**********0: JSP_Course_zj
**********1: Java_OJ


1887140233


gaoru188


1881140216


zrqking


1881140213


cURL
**********0: AcmLab
**********1: lec
**********2: canvas
**********3: domains
**********4: calculator


IcewithaT


Beyound_zain
**********0: Oj
**********1: test
**********2: CLASS


1881140136


X


741741


nihuifeima


Wang


Windows


xh


1884140111


1884140139


1884140138


1884140117


1884140227


rzx1884140136


nickJacky


1884140222


duanyafei


1884140102


wang-feng


1881140235


ChenZJ


方博飞


1887140140


YuanLD


Jerry


1884140228


yishengchen


Belmode
**********0: AHSTU_OJ
**********1: WiFiViewer


bfmiaodi


lgs


1884140137


wildbird


dongjie
**********0: java
**********1: AOJ


LIDie
**********0: SharedPreferencesTest
**********1: Broadcast


1881140107



124
'''