import math, tkinter
coords, n = [], int(input())
for k in range(1, n+1): coords.append((300+200*math.cos((2*math.pi*k)/n), 300+200*math.sin((2*math.pi*k)/n)))
master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)
this, Next, step, i = False, False, len(coords)//2, 0
if n % 2 == 0: step = step -1
for i in range(len(coords)):
    if i >= len(coords): this = coords[i - len(coords)]
    else: this = coords[i]
    if i+step >= len(coords): Next = coords[i+step - len(coords)]
    else: Next = coords[i+step]
    canvas.create_line(this, Next, fill='#005500')
    Next = coords[i-step]
    canvas.create_line(this, Next, fill='#005500')    
canvas.pack()
master.mainloop()
