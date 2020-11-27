from collections import defaultdict
maxddegree=defaultdict()
rowcountzero=[]
colcountzero=[]
maxlist=[]
def rzerocount(bo):
    rcount=0
    for r in range(len(bo)):
        j=0
        while(j<len(bo)):
            if(bo[r][j]==0):
                rcount+=1
                j+=1
            else:
                j+=1
        rowcountzero.append(rcount)
        rcount=0
def czerocount(bo):
    rcount=0
    for r in range(len(bo)):
        j=0
        while(j<len(bo)):
            if(bo[j][r]==0):
                rcount+=1
                j+=1
            else:
                j+=1
        colcountzero.append(rcount)
        rcount=0
def maxddegreecount(bo):
    for i in range(len(bo)):
        for j in range(len(bo)):
            if(bo[i][j]==0):
                maxddegree[i,j]=rowcountzero[i]+colcountzero[j]-2
    sort_orders = sorted(maxddegree.items(), key=lambda x: x[1], reverse=False)
    for k in sort_orders:
        #print(k[0])
        maxlist.append(k[0])
    #for k,v in maxddegree.items():
        #print(k,v)
def deg():
    return maxddegree.items()
def maxddegreeempty():
    if(len(maxlist)==0):
        return None
    else:
        val=maxlist.pop(0)
        i=val[0]
        j=val[1]
    return (i,j)
"""with open('input1.txt', 'r') as f:
    board = [[int(num) for num in line.split(',')] for line in f]
rzerocount(board)
czerocount(board)
maxddegreecount(board)
"""