import tkinter as tk
import random

root = tk.Tk()
root.geometry("601x640")

c = tk.Canvas(root, height=601, width=601, bg='WHITE',borderwidth=0, highlightthickness=0)
c.grid(row=0,column=0)

def DrawGrid(board,noOfGrids):
    size = 600/noOfGrids
    width = 1
    gap = 0
    for j in range(0,int(600/size)):
        for i in range(0,int(600/size)):
            if board[i][j] == 1:
                fill = 'black'
                c.create_rectangle(i*size+gap,j*size+gap,i*size+size,j*size+size,width=width,outline="black",fill=fill)
            #else:
                #fill = 'white'
                #fill= 'bisque3'
                #c.create_rectangle(i*size+gap,j*size+gap,(i*size+size),(j*size+size),width=width,outline="black",fill=fill)

def CountNeighbour(matrix, r, c):
    def get(r, c):
        if 0 <= r < len(matrix) and 0 <= c < len(matrix[r]):
            return matrix[r][c]
        else:
            return 0

    neighbors_list = [get(r-1, c-1), get(r-1, c), get(r-1, c+1),
                      get(r  , c-1),              get(r  , c+1),
                      get(r+1, c-1), get(r+1, c), get(r+1, c+1)]

    return sum(neighbors_list)

def SimulateGameOfLife(board,noofgrids):
    for i in range(noofgrids):
        for j in range(noofgrids):
            print(CountNeighbour(board,i,j),end=" ")
            
        
def CreateGrid(noofgrids):
    board = [[int(random.choice([0,1])) for x in range(noofgrids)] for x in range(noofgrids)]
    i = int(noofgrids/2)
    j = int(noofgrids/2)
    board[i][j]=1
    DrawGrid(board,noofgrids)
    
    SimulateGameOfLife(board,noofgrids)
        

noofgrids = 20
CreateGrid(noofgrids)

root.mainloop()