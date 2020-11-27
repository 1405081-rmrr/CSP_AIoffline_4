from collections import defaultdict
import importlib
from maximumDegree import rzerocount,czerocount,deg,maxddegreecount,maxddegreeempty
#from Domdeg import domdegfunc,domdegratio
import time
start=time.time()
li=[]
count=0
fcount=0
superlist=[]
tnode=0
domi=[]
degg=[]
rat=[]
ratio=defaultdict()
ratmin=[]

def boardlen(board):
    for i in range(1,len(board)+1):
        li.append(i)
rowc=defaultdict(list)
colc=defaultdict(list)
rowcoldata=defaultdict(list)
location=defaultdict()
sort_orders=defaultdict()
maxddegree=defaultdict()
count=0
def rowdata(bo):
    for r in range(len(bo)):
        j=0
        while(j<len(bo)):
            if(bo[r][j]!=0):
                rowc[r].append(bo[r][j])
                j+=1
            else:
                j+=1
    #for k,v in rowc.items():
        #print(k,v)

def coldata(bo):
    for r in range(len(bo)):
        j=0
        while(j<len(bo)):
            if(bo[j][r]!=0):
                colc[r].append(bo[j][r])
                j+=1
            else:
                j+=1
    #for k,v in colc.items():
        #print(k,v)
def show(bo):
    final=[]
    count=0
    p=[]
    q=[]
    r=[]
    for k in rowc.keys():
        p = rowc.get(k).copy()
        for j in colc.keys():
            if(bo[k][j]==0):
                q=colc.get(j).copy()
                r=p+q
                final=diff(li,r)
                for rr in final:
                    rowcoldata[k,j].append(rr)

                rowcoldata[k,j].sort()
                list(set(rowcoldata[k,j]))
                r.clear()
                q.clear()
        p.clear()
    for k,v in rowcoldata.items():
        #print(k,v)
        location[k]=len(v)
    print()
    sort_orders = sorted(location.items(), key=lambda x: x[1], reverse=False)
    #sort_orders = sorted(location.items(), key=lambda x: x[1], reverse=False)
    for x in sort_orders:
        superlist.append(x[0])
def dom():
    return location.items()

def diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif
def solve(bo):
    global tnode
    global fcount
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,len(bo)+1):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            tnode+=1


            if solve(bo):
                return True

            bo[row][col] = 0


    fcount = countback()
    tnode+=1
    return False
def countback():
    global count
    count=count+1
    return count
def solveBT_SDF(bo):
    global fcount
    global tnode
    find = find_empty(bo)
    bilai=empty()
    if not find:
        return True
    elif(not bilai):
        row,col=find
    else:
        row,col=bilai


    for i in range(1,len(bo)+1):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            tnode += 1


            if solveBT_SDF(bo):
                return True

            bo[row][col] = 0
            #fcount=countback()
    fcount = countback()
    tnode += 1
    return False
def solveBT_MaxDDegree(bo):
    global fcount
    global tnode
    find = find_empty(bo)
    bilai=maxddegreeempty()
    if not find:
        return True
    elif(not bilai):
        row,col=find
    else:
        row,col=bilai



    for i in range(1,len(bo)+1):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            tnode += 1


            if solveBT_MaxDDegree(bo):
                return True

            bo[row][col] = 0
            #fcount=countback()
    fcount = countback()
    tnode += 1
    return False
def domdegfunc():
    domain = dom()
    degree = deg()
    for k in domain:
    #print(k[0],k[1])
        domi.append(k[1])
    for k in degree:
    #print(k[0],k[1])
        degg.append(k[1])
    for i,j in zip(domi,degg):
        rat.append(i/j)
    for k ,x in zip(domain,rat):
        ratio[k[0]]=x
    sort_orders = sorted(ratio.items(), key=lambda x: x[1], reverse=False)
    for x in sort_orders:
        ratmin.append(x[0])
def domdegratio():
    if(len(ratmin)==0):
        return None
    else:
        val=ratmin.pop(0)
        i=val[0]
        j=val[1]
    return (i,j)
def solveBT_Domddeg(bo):
    global fcount
    global tnode
    find = find_empty(bo)
    bilai=domdegratio()
    if not find:
        return True
    elif(not bilai):
        row,col=find
    else:
        row,col=bilai



    for i in range(1,len(bo)+1):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            tnode += 1


            if solveBT_Domddeg(bo):
                return True

            bo[row][col] = 0
            #fcount=countback()
    fcount = countback()
    tnode += 1
    return False

def empty():
    if(len(superlist)==0):
        return None
    else:
        val=superlist.pop(0)
        i=val[0]
        j=val[1]
    return (i,j)
def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        p=pos[0]
        if bo[p][i] == num :
            return False

    # Check column
    for i in range(len(bo)):
        q=pos[1]
        if bo[i][q] == num :
            return False

    return True
def print_board(bo):
    for i in range(len(bo)):

        for j in range(len(bo[0])):

            if j == len(bo)-1:
                print(bo[i][j])
            else:
                #print(str(bo[i][j]) +" ",end="")
                print(bo[i][j],"",end="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                #return True
                return (i,j) # row, col

    return None

#print_board(board)
with open('input2.txt', 'r') as f:
    board = [[int(num) for num in line.split(',')] for line in f]
print()
print("1. BT+Random 2. BT+SDF 3. BT+MaxDDegree 4.BT+Domddeg")
n=int(input())
if(n==1):
    boardlen(board)
    solve(board)
    print("BT+Random")
    print_board(board)
    print("Backtracking Counted : ",fcount)
    print("Nodes : {}".format(tnode))


if(n==2):
    boardlen(board)
    rowdata(board)
    coldata(board)
    show(board)
    #dom()
    deg()
    solveBT_SDF(board)
    print("BT+SDF")
    print_board(board)
    print("Backtracking counted : ",fcount)
    print("Nodes : {}".format(tnode))
if(n==3):
    rzerocount(board)
    czerocount(board)
    maxddegreecount(board)
    #deg()
    solveBT_MaxDDegree(board)
    print("BT+MaxDyanmicDegree")
    print_board(board)
    print("Backtracking counted for MaxDDegree : ", fcount)
    print("Nodes : {}".format(tnode))
if(n==4):
    rzerocount(board)
    czerocount(board)
    maxddegreecount(board)
    domdegfunc()
    solveBT_Domddeg(board)
    print("BT+DomDynamicDegree")
    print_board(board)
    print("Backtracking counted for DomDDeg : ", fcount)
    print("Nodes : {}".format(tnode))


print("Time Taken {}".format(time.time() - start))