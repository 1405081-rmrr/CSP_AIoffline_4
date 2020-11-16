from collections import defaultdict
board = [
[0, 0, 6, 0, 0, 3, 4, 0, 10, 0 ],
[2, 6, 4, 0, 0, 0, 0, 0, 9, 0 ],
[0, 2, 10, 0, 0, 0, 0, 0, 5, 9 ],
[10, 1, 5, 4, 2, 0, 0, 0, 0, 0 ],
[0, 0, 0, 0, 1, 9, 8, 4, 0, 0 ],
[0, 0, 3, 2, 9, 0, 0, 1, 0, 0],
[6, 0, 0, 0, 0, 7, 0, 10, 0, 5 ],
[0, 0, 0, 0, 0, 8, 6, 5, 0, 7 ],
[1, 3, 0, 6, 0, 0, 5, 0, 0, 2 ],
[0, 5, 0, 9, 6, 2, 0, 0, 8, 0 ]
]
li=[]
faka=defaultdict(list)
for i in range(1,len(board)+1):
    li.append(i)
file=open("balchal","w")
rowc=defaultdict(list)
colc=defaultdict(list)
rowcoldata=defaultdict(list)
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
def zero(bo):
    count=0
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if(bo[i][j]==0):
               return (i,j)

    return None
def coldata(bo):
    for r in range(len(bo)):
        j=0
        while(j<len(bo)):
            if(bo[j][r]!=0):
                colc[r].append(bo[j][r])
                j+=1
            else:
                j+=1
    for k,v in colc.items():
        print(k,v)
def duplicacy(li1,li2):
    for num in li2:
        if(li1==num):
            return False
    return True


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
                if duplicacy(rr,rowcoldata[k,j]):
                    rowcoldata[k,j].append(rr)
            rowcoldata[k,j].sort()
            r.clear()
            q.clear()
        p.clear()
    #for k,v in rowcoldata.items():
        #print(k,v)
def advance(bo):
    v=[]
    p=[]
    q=[]
    r=[]
    element=[]
    for m in range(len((bo))):
        for n in range(len(bo[0])):
            if(bo[m][n]==0):
                p=rowc.get(m).copy()
                q=colc.get(n).copy()
                r=p+q
                #print(r)
                element=diff(li,r)
                for e in element:
                    faka[m,n].append(e)
    for k, v in faka.items():
        print(k,v)
        if(len(v)==1):
            s=k[0]
            t=k[1]
            man=v[0]
            bo[s][t]=man
    solve(bo)
def solve(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            file.write(str(bo[i][j]))
            file.write(' ')
        file.write('\n')
    file.write('\n')
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,len(bo[0])+1):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False
def diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif
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
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

print_board(board)
print("___________________")

print("___________________")
rowdata(board)
print("___________________")
coldata(board)
print("___________________")
show()
advance(board)
print("___________________")
#coldata(board)
#solve(board)
print("___________________")
print("___________________")
print_board(board)
