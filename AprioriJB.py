import collections as cc
from itertools import combinations

def innerJoin(temp):
    freq = cc.defaultdict(int)
    for i in range(len(temp)):
        for j in range(i+1,len(temp)):
            if list(list(temp.keys())[i][:len(list(temp.keys())[i])-1:]) == list(list(temp.keys())[j][:len(list(temp.keys())[j])-1:]):
                dummy = list(list(temp.keys())[i])
                dummy.append(list(temp.keys())[j][-1])
                freq[tuple(dummy)] = 0
    return freq

def itemSet(temp):  
    freq = cc.defaultdict(int)      
    for i in temp:
        for j in dic:
            if set(i).issubset(set(dic[j])):
                freq[i] += 1
    return freq
        
def checkSigma(freq):
    temp = cc.defaultdict(int)
    for i in sorted(freq):
        if freq[i] >= sigma:
            temp[i] = freq[i]
    return temp

dic = cc.defaultdict(list)
#dic = {10:['A','C','D','E'], 20:['B','C','E'], 30:['A','B','C','E'], 40:['B','E']}

file = open("C:\\Users\\Admin\\Desktop\\DM_LabTest1\\ps6data.txt",'r')
lines = file.readlines()

for i in range(len(lines)):
    dic[i] = list(lines[i].rstrip('\n').split(';'))    

sigma = 2

freq = cc.defaultdict(int)

ans = []

for i in dic:
    for j in dic[i]:
        freq[j] += 1
ans.append(checkSigma(freq))
freq = cc.defaultdict(int)
comb = combinations(ans[0].keys(), 2)
freq = itemSet(comb)          
ans.append(checkSigma(freq))

while(1):
    if len(ans[-1]) <= 1:
        break
    freq = cc.defaultdict(int)
    freq = innerJoin(ans[-1])    
    temp = checkSigma(itemSet(sorted(freq)))
    if len(temp) > 0:
        ans.append(temp)
    else:
        break
print(ans)
con = []
for i in ans[-1]:
    conf = cc.defaultdict(float)
    for j in range(1,len(ans)):
        c = combinations(i, j)
        for k in c:
            if len(k) == 1:
                conf[''.join(k)] = ans[-1][i]/ans[j-1][''.join(k)]*100
            else:
                conf[k] = ans[-1][i]/ans[j-1][k]*100
    con.append(conf)
print(con)