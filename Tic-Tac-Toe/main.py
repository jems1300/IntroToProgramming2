from tkinter import *


class Cell(Label):
    def __init__(self, container):
        Label.__init__(self, container, image=imageEmpty)
        self.token = " "
        self.bind("<Button-1>", self.flip)

    def flip(self, event):
        global currentToken  # [X, O, Over]
        if self.token == " " and currentToken != "Over":
            if currentToken == "X":
                currentToken = "O"
                self.token = "O"
                self["image"] = imageX
            else:
                self.token = "O"
                self["image"] = imageO
                currentToken = "X"

        checkStatus(self.token)

def checkStatus(token):
    global currentToken
    if isWon(token):
        statusLabel["text"] = token + "won!"
        currentToken = "Over"

    elif isFull():


def isFull():
    full = True
    for i in range(3):
        for j in range(3):
            if cells[i][j].token == " ":
                full = False
    return full

def isWon(token):
    for i in range(3):
        if cells[i][0].token == token and cells[i][1].token == cells[i][2].token:
            return True

    for j in range(3):
        if cells[0][j].token == token and cells[1][j].token ==

# game window
window = Tk()
window.title("Game")

# load images
imageEmpty = PhotoImage(file="./image/empty.gif")
imageX = PhotoImage(file="./image/empty.gif")
imageO = PhotoImage(file="./image/empty.gif")

# Frames holding the 3x3 cells
frame = Frame(window)
frame.pack()

cells = []
for i in range(3):
    cells.append([])
    for j in range(3):
        cells[i].append(Cell(frame))
        cells

# This attaches it to the window

statusLabel = Label(window, text="continue")
statusLabel.pack()

window.mainloop()
