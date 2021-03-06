# Python program to solve N Queen
# Problem using backtracking
import collections
global N
N = 8
location=collections.defaultdict(list)
def printSolution(board):
    for i in range(N):
        for j in range(N):
            if(board[i][j]==-1):
                board[i][j]=0
            print(board[i][j],end=" ")
        print()

def solveNQUtil(board, col):
    r1=0
    c1=0
    if col >= N:
        return True

    for i in range(N):

        if (board[i][col]!=-1):

            board[i][col] = 1
            for c2 in range(col+1,N,1):
                if(board[i][c2]==-1):

                    continue
                board[i][c2]=-1
                location[col].append((i,c2))

            r1=i+1
            c1=col+1
            while(r1<N and c1<N):
                if(board[r1][c1]==-1):
                    r1 = r1 + 1
                    c1 = c1 + 1
                    continue
                board[r1][c1]=-1
                location[col].append((r1, c1))
                r1 = r1 + 1
                c1 = c1 + 1
            r1=0
            c1=0
            r1 = i - 1
            c1 = col + 1
            while (r1 >=0 and c1 < N):
                if (board[r1][c1] == -1):
                    r1 = r1 - 1
                    c1 = c1 + 1
                    continue
                board[r1][c1] = -1
                location[col].append((r1, c1))
                r1 = r1 -1
                c1 = c1 + 1
            print("After Safe ...")
            for v in range(N):
                for w in range(N):
                    print(board[v][w], end=" ")
                print()
            print("After locating...")
            for k,v in location.items():
                print(k,v)
            # recur to place rest of the queens
            if solveNQUtil(board, col + 1) == True:
                return True
            board[i][col] = 0
            for k in location.keys():
                if(k==col):
                    for v in location.get(k):
                        rowcol=v
                        row=rowcol[0]
                        column=rowcol[1]
                        board[row][column]=0
            location[col].clear()
            print("After backtracking...")
            for v in range(N):
                for w in range(N):
                    print(board[v][w],end=" ")
                print()
            print()

    return False
def solveNQ():
	board = [ [0, 0, 0, 0,0,0,0,0],
			[0, 0, 0, 0,0,0,0,0],
			[0, 0, 0, 0,0,0,0,0],
			[0, 0, 0, 0,0,0,0,0],
              [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]
			]

	if solveNQUtil(board, 0) == False:
		print ("Solution does not exist")
		return False

	printSolution(board)
	return True

solveNQ()


