import numpy as np
import random
board=[]


for i in range(3):
  a=[]
  for j in range(3):
    a.append('-')
  print() 
  board.append(a)
#to reshape the matrix
board=np.reshape(board,(3,3))

#print(board) to check if the board is printing correct

def check(r,c):
# assigning the grid location to compare with the location where either X or 0 is inserted  
  A=board[0][0]
  B=board[0][1]                     # A|B|C
  C=board[0][2]                     # D|E|F
  D=board[1][0]                     # G|H|I
  E=board[1][1]
  F=board[1][2]
  G=board[2][0]
  H=board[2][1]
  I=board[2][2]
  
  while(True):
    if A==board[r-1][c-1]:
      #condition to check for diagonal, vertical and horizontal series of XXX or 000
      if (A==B and A==C )or (A==E and A==I) or (A==D and A==G):
        print("Win")
        print(board)
        break
      #else it will decide whom to give next move to  
      else:
        if(A=='x'):
          chance_y()
        elif(A=='0'):
          chance_x()
      
    elif B==board[r-1][c-1]:
      if (B==A and B==C) or (B==E and B==H):
        print("Win")
        print(board)
        break
      else:
        if(B=='x'):
          chance_y()
        elif(B=='0'):
          chance_x()

    elif C==board[r-1][c-1]:
      if (C==A and C==B) or (C==F and C==I) or (C==E and C==G):
        print("Win")
        print(board)
        break
      else:
        if(C=='x'):
          chance_y()
        elif(C=='0'):
          chance_x()
      
    elif D==board[r-1][c-1]:
      if (D==A and D==G) or (D==E and D==G):
        print("Win")
        print(board)
        break
      else:
        if(D=='x'):
          chance_y()
        elif(D=='0'):
          chance_x()

    elif E==board[r-1][c-1]:
      if (E==B and E==H) or (E==A and E==I) or (E==C and E==G):
        print("Win")
        print(board)
        break
      else:
        if(E=='x'):
          chance_y()
        elif(E=='0'):
          chance_x()

    elif F==board[r-1][c-1]:
      if (F==C and F==I) or (F==E and F==D):
        print("Win")
        print(board)
        break
      else:
        if(F=='x'):
          chance_y()
        elif(F=='0'):
          chance_x()

    elif G==board[r-1][c-1]:
      if (G==A and G==D) or (G==H and G==I) or (G==E and G==C):
        print("Win")
        print(board)
        break
      else:
        if(G=='x'):
          chance_y()
        elif(G=='0'):
          chance_x()

    elif H==board[r-1][c-1]:
      if (H==G and H==I) or (H==E and H==B):
        print("Win")
        print(board)
        break
      else:
        if(H=='x'):
          chance_y()
        elif(H=='0'):
          chance_x()

    elif I==board[r-1][c-1]:
      if (I==C and I==F) or (I==G and I==H) or (I==A and I==E):
        print("Win")
        print(board)
        break
      else:
        if(I=='x'):
          chance_y()
        elif(I=='0'):
          chance_x()
    #breaking the while loop.
    break

def chance_x():
  #taking inputs from the user.
  print(board)
  r=int(input("Enter the row you want to enter x:"))
  c=int(input("Enter the column you want to enter x:"))
  board[r-1][c-1]='x'
  check(r,c)
  

def chance_y():
  print(board)
  list=[1,2,3]
  r=random.choice(list)
  c=random.choice(list)
  if board[r-1][c-1]=='-':
    board[r-1][c-1]='0'
    check(r,c)
  else:
    r=random.choice(list)
    c=random.choice(list)
    board[r-1][c-1]='0'
    check(r,c)


chance_x()
