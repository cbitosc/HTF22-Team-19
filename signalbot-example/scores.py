from espncricinfo.summary import Summary
from espncricinfo.match import Match

#s = Summary()
#matchesArr = s._build_matches()
matArr = ['1330732', '1330733', '1330734', '1330735', '1330739', '1330740', '1330730', '1330731', '1330737', '1330729', '1330736', '1322402', '1298162', '1342070', '1342071', '1323577', '1333046', '1333047', '1336280', '1298163', '1335466', '1335467', '1298164', '1333048', '1342113', '1334914', '1342114']
def fun():
    ans = ''
    ans += "List of Recent Matches:\n"
    for i,j in zip(matArr,range(8)):
        ans += str(j) + ")  " + Match(i).description + '\n'
        ans += '    ' + Match(i).current_summary + '\n'
    return ans
def getScore(i):
    ans = ''
    ans += "Score for" + Match(matArr[i]).description + "is:\n"
    ans += Match(matArr[i]).current_summary + "\n"
    return ans
