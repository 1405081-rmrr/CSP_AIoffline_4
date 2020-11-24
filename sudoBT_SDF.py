from collections import defaultdict
board = [
    [0, 0, 6, 0, 0, 3, 4, 0, 10, 0 ],
    [2, 6, 4, 0, 0, 0, 0, 0, 9, 0 ],
    [0, 2, 10, 0, 0, 0, 0, 0, 5, 9 ],
    [10, 1, 5, 4, 2, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 1, 9, 8, 4, 0, 0 ],
    [0, 0, 3, 2, 9, 0, 0, 1, 0, 0 ],
    [6, 0, 0, 0, 0, 7, 0, 10, 0, 5 ],
    [0, 0, 0, 0, 0, 8, 6, 5, 0, 7 ],
    [1, 3, 0, 6, 0, 0, 5, 0, 0, 2 ],
    [0, 5, 0, 9, 6, 2, 0, 0, 8, 0]
]
li=[]
superlist=[]
for i in range(1,len(board)+1):
    li.append(i)
rowc=defaultdict(list)
colc=defaultdict(list)
rowcoldata=defaultdict(list)
location=defaultdict()
sort_orders=defaultdict()
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
    sort_orders = sorted(location.items(), key=lambda x: x[1], reverse=False)
    for x in sort_orders:
        superlist.append(x[0])
    """for x in sort_orders:
        count=count+1
        print(x[0],x[1])
    print(count)
    """






def diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,len(bo)+1):
        if valid(bo, i, (row, col)):
            bo[row][col] = i


            if solve(bo):
                return True

            bo[row][col] = 0


    return False
def solveBT_SDF(bo):
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


            if solveBT_SDF(bo):
                return True

            bo[row][col] = 0
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
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                #return True
                return (i,j) # row, col

    return None

print_board(board)
print()
print("1. BT+Random 2. BT+SDF ")
n=int(input())
if(n==1):
    rowdata(board)
    coldata(board)
    show(board)
    solve(board)
    print_board(board)
if(n==2):
    rowdata(board)
    coldata(board)
    show(board)
    solveBT_SDF(board)
    print_board(board)