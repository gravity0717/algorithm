import sys 


N ,M = map(int,input().split())

dx = [2,1,-1,-2]
dy = [1,2,1,2]

chessboard  = [[0]*N for _ in range(M)]

chessboard[0][0] =1 

    