from espncricinfo.summary import Summary
from espncricinfo.match import Match
import re
#s = Summary()
#matchesArr = s._build_matches()
matArr = ['1330732', '1330733', '1330734', '1330735', '1330739', '1330740', '1330730', '1330731', '1330737', '1330729', '1330736', '1322402', '1298162', '1342070', '1342071', '1323577', '1333046', '1333047', '1336280', '1298163', '1335466', '1335467', '1298164', '1333048', '1342113', '1334914', '1342114']
m = Match(matArr[0])
wickets = score = ''
score = m.current_summary.split('/')
for j in score[0]:
    if j.isnumeric():
        score += j;
for j in score[1]:
    if j.isnumeric():
        wickets += j;
print('wickets:',wickets,'score:',score)        
