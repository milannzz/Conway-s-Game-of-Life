import tkinter as tk
from tkinter import Label, Spinbox, ttk
import random

# Clearer Ui using ctypes
import ctypes
from typing import Text
ctypes.windll.shcore.SetProcessDpiAwareness(1)

root = tk.Tk()
root.geometry("801x850")
root.title("Convay's Game Of Life")
root.resizable(0,0)

c = tk.Canvas(root, height=801, width=801, bg='WHITE',borderwidth=0, highlightthickness=0)
c.grid(row=0,column=0)

def DrawGrid(board,noOfGrids):
    size = 800/noOfGrids
    width = 1
    gap = 0
    for i in range(0,int(800/size)):
        for j in range(0,int(800/size)):
            if board[i][j] == 0:
                fill = 'white'
                c.create_rectangle(i*size+gap,j*size+gap,i*size+size,j*size+size,width=width,outline="white",fill=fill)
                #c.create_text(i*size+int(size/2),j*size+int(size/2),text=board[i][j])

            elif board[i][j] == 1:
                fill = 'black'
                c.create_rectangle(i*size+gap,j*size+gap,i*size+size,j*size+size,width=width,outline="white",fill=fill)
                #c.create_text(i*size+int(size/2),j*size+int(size/2),text=board[i][j],fill="white")
    root.update_idletasks()

def CountNeighbour(matrix, r, c):
    def get(r, c):
        root.update()
        if 0 <= r < len(matrix) and 0 <= c < len(matrix[r]):
            return matrix[r][c]
        else:
            return 0

    neighbors_list = [get(r-1, c-1), get(r-1, c), get(r-1, c+1),
                      get(r  , c-1),              get(r  , c+1),
                      get(r+1, c-1), get(r+1, c), get(r+1, c+1)]

    return sum(neighbors_list)

def GameOfLife(board,noofgrids):
    for i in range(noofgrids):
        for j in range(noofgrids):
            root.update()
            if board[i][j] == 1 :
                if CountNeighbour(board,i,j) > 3:
                    board[i][j] = 0
                elif CountNeighbour(board,i,j) < 2 :
                    board[i][j] = 0
                else :
                    board[i][j] = 0

            elif board[i][j] == 0 :
                if CountNeighbour(board,i,j) == 3:
                    board[i][j] = 1
       
def RandomizeTheGrid():
    noofgrids = noSpin.get()
    board = [[random.choice([0,1]) for x in range(noofgrids)] for x in range(noofgrids)]
    DrawGrid(board,noofgrids)
    while(1):   
        root.update()
        GameOfLife(board,noofgrids)
        DrawGrid(board,noofgrids)

def SimulateGameOfLife():
    pass
    """
        while(1):
            root.update()
            GameOfLife(board,noofgrids)
            DrawGrid(board,noofgrids)
    """

def Exit():
    root.destroy()

noSpin = tk.IntVar()
noSpin.set(30)

frame = tk.Frame(root)
frame.grid(row=1,column=0,padx=10,pady=10)

Label(frame,text="Dimensions NxN :").grid(row= 0, column= 0,padx= 8,pady= 2)

spinbox = tk.Spinbox(frame,textvariable=noSpin,from_=2,to=1000,increment=2,width=12,font="arial 9")
spinbox.grid(row=0,column=1,padx=8,pady=2)

buttonRandom = tk.Button(frame,text="Randomize",command=RandomizeTheGrid,width=12,font="arial 9")
buttonRandom.grid(row=0,column=2,padx=8,pady=2)

buttonRandom = tk.Button(frame,text="Start the Life ",command=SimulateGameOfLife,width=12,font="arial 9",state=tk.DISABLED)
buttonRandom.grid(row=0,column=3,padx=8,pady=2)

buttonStop = tk.Button(frame,text="Exit",command=Exit,fg="white",bg="red",width=12,font="arial 9")
buttonStop.grid(row=0,column=4,padx=8,pady=2)

root.mainloop()