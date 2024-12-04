import tkinter
main = tkinter.Tk(className='Chess')
canvas = tkinter.Canvas(main, bg='white', height=600, width=600)
past = [2,2]
for j in range(1,9):
    for i in range(0, 8, 2):
        if j % 2 == 0:
            canvas.create_rectangle((past[0], past[1]), (past[0]+74, past[1]+74), fill='#663333')
            past[0], past[1] = past[0]+74, past[1]
        canvas.create_rectangle((past[0], past[1]), (past[0]+74, past[1]+74))
        past[0], past[1] = past[0]+74, past[1]
        if j % 2 != 0:
            canvas.create_rectangle((past[0], past[1]), (past[0]+74, past[1]+74), fill='#663333')
            past[0], past[1] = past[0]+74, past[1]        
        
    past = [2, past[1]+74]
canvas.pack()
main.mainloop()