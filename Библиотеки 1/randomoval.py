import tkinter, random


def draw(event):
    X, Y, r = random.randint(0, 600), random.randint(10, 600), random.randint(1, 300)
    canvas.create_oval((Y, X), (Y+r, X+r), fill='red')
    return

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='#000', height=600, width='blue')
canvas.pack()
master.bind("<KeyPress>", draw)
master.mainloop()