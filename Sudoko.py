from collections import defaultdict
from itertools import permutations
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
rowc=defaultdict(list)
colc=defaultdict(list)
rowcoldata=defaultdict(list)
row = []
col=[]
getrow=[]
def rowdata(bo):
    for r in range(len(bo)):
        j=0
        while(j<len(bo)):
            if(bo[r][j]!=0):
                rowc[r].append(bo[r][j])
                j+=1
            else:
                j+=1
    for k,v in rowc.items():
       print(k,v)

def coldata(bo):
    for r in range(len(bo)):
        j=0
        while(j<len(bo)):
            if(bo[j][r]!=0):
                colc[r].append(bo[j][r])
                j+=1
            else:
                j+=1

def show():
    p=[]
    q=[]
    r=[]
    for k in rowc.keys():
        p = rowc.get(k).copy()
        for j in colc.keys():
            q=colc.get(j).copy()
            r=p+q
            for rr in r:
                rowcoldata[k,j].append(rr)

            rowcoldata[k,j].sort()
            list(set(rowcoldata[k,j]))
            r.clear()
            q.clear()
        p.clear()

def solution(bo):
    li=[]
    perm=[]
    row = []
    getrow = []
    for l in range(1,len(bo)+1):
        li.append(l)
    for k in rowc.keys():
        row=[]
        getrow=[]
        row.clear()
        getrow.clear()
        row=rowc.get(k).copy()
        getrow=diff(li,row)
        perm=permutations(getrow)
        matchcol((list(perm)),bo,k)


def diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif
def matchcol(perm,bo,r):
    for c in range(len(bo[0])):
        if(bo[r][c]==0):
            col.append(c)
    print("Column No ",col)
    valid(perm,col,r,bo)
    col.clear()



def valid(per,li,rownum,bo):
    index=0
    flag=0
    tupi=[]
    for tup in per:
        print("Tuple : ",tup)
        for t in tup:
            print("Data :",t)
            if(checkcol(t,li[index])==True):
                index=index+1
                print("Index ",index)
                flag=flag+1
                tupi.append(t)
            else:
                index=0
                tupi.clear()
                flag=0
                break
        if(index==len(li)):
            break
    print("Rslt ",tupi)
    index=0
    for column in li:
        bo[rownum][column] = tupi[index]
        colc[column].append(tupi[index])
        index+=1
    for rlt in tupi:
        rowc[rownum].append(rlt)
    print(rowc.get(rownum))
    for column in li:
        print(colc.get(column))
    for ba in range(len(bo)):
        for cha in range(len(bo[0])):
            print(bo[ba][cha],end=" ")
        print()





def checkcol(num,column):
    columnlist=[]
    columnlist=colc.get(column).copy()
    for colnum in columnlist:
        if(colnum==num):
            return False
    return True
def print_board(bo):
    for i in range(len(bo)):

        for j in range(len(bo[0])):

            if j == len(bo)-1:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

print_board(board)
print("___________________")

rowdata(board)
print("___________________")
coldata(board)
print("___________________")
show()
solution(board)

#solve(board)
print("___________________")
print("___________________")
print_board(board)
