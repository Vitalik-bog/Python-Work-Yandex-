import tkinter

def key_pressed(event):
    if event.keysym == 'space':
        canvas.coords(oval, (300, 300, 310, 310))    
    if event.keysym == 'Up':
        canvas.move(oval, 0, -10)
    elif event.keysym == 'Down':
        canvas.move(oval, 0, 10)
    elif event.keysym == 'Left':
        canvas.move(oval, -10, 0)
    elif event.keysym == 'Right':
        canvas.move(oval, 10, 0)
    if canvas.coords(oval)[0] > COORDS[0] + 100 or canvas.coords(oval)[1] > COORDS[1] + 100 or canvas.coords(oval)[0] < COORDS[0] - 100 or canvas.coords(oval)[1] < COORDS[1] - 100:
        canvas.itemconfig(oval, fill='red')
    else:
        canvas.itemconfig(oval, fill='green')
    

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
oval = canvas.create_oval((300, 300), (310, 310), fill='green')
COORDS = canvas.coords(oval)
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()