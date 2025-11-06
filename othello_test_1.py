import numpy as np
import sys

def kaishi():
    

def teigi(board):
    for i in range(8):
        for j in range(8):
            if(board[j][i]==0):
                print(" ",end='')
            if(board[j][i]==-1):
                print("●",end='')
            if(board[j][i]== 1):
                print("○",end='')
    print()
    
def board_init(board):
    board = np.zeros((8,8))
    board[3][3]= 1
    board[3][4]=-1
    board[4][3]=-1
    board[4][4]= 1
    return board

def judge(board,bw,rowcol):
    i=1
    j=1
    cnt=0
    ok=0
    way=0
    if(1>rowcol[0] or 8<rowcol[0] or 1>rowcol[1] or 8<rowcol[1]):
        print('存在しないマスです。')
        return 1
    
    for way in range(1,9):
        cnt=0
        if(way==1 or way==2):
            i=0
        if(way==3 or way==5 or way==6):
            i=1
        if(way==4 or way==7 or way==8):
            i=-1
def check(board,bw):
    cnt_black=0
    cnt_white=0
    for i in range(8):
        for j in range(8):
            if(board[j][i]==-1):
                cnt_black+=1
            if(board[j][i]== 1):
                cnt_white+=1
    if(bw==-1):
        return cnt_black
    if(bw==1):
        return cnt_white
    
    