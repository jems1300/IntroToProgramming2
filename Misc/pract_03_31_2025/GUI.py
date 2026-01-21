import tkinter as tk

window = tk.Tk()

window.title("Fuck you")
window.geometry("1920x1080")

label = tk.Label(window, text = "Fuck you too")
label.pack() #Display the label in the window

def button_press():
    print("Alright")# prints this in the console
    exit()

def button_press2():
    label2 = tk.Label(window, text= "nvm fuck you")
    label2.pack()

button = tk.Button(window, text = "Fuck you i don't do anything", command=button_press)
button.pack() #<- from what i understand this just attaches it

button2 = tk.Button(window, text = "I feel like being nice", command = button_press2)
button2.pack()

def update_text():
    label.config(text="i am so lonely")

#bind mouse event
button.bind("<Button-1>", update_text)
window.mainloop()

#TK class represents the main window within a GPU application