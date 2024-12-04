import tkinter
main = tkinter.Tk(className='Chess')
canvas = tkinter.Canvas(main, bg='#E5D5C3', height=600, width=600)
past = [2,2]
for j in range(1,6):
    for i in range(0, 7, 2):
        if j % 2 == 0:
            canvas.create_rectangle((past[0], past[1]), (past[0]+74, past[1]+74), fill='#7F705D')
            if j < 3:
                canvas.create_oval((past[0], past[1]), (past[0]+74, past[1]+74), fill='#fff')
            past[0], past[1] = past[0]+74, past[1]
        canvas.create_rectangle((past[0], past[1]), (past[0]+74, past[1]+74))
        past[0], past[1] = past[0]+74, past[1]
        if j % 2 != 0:
            canvas.create_rectangle((past[0], past[1]), (past[0]+74, past[1]+74), fill='#7F705D')
            if j < 5:
                canvas.create_oval((past[0], past[1]), (past[0]+74, past[1]+74), fill='#fff')
            past[0], past[1] = past[0]+74, past[1]          
    past = [2, past[1]+74]
for j in range(1,4):
    for i in range(0, 7, 2):
        if j % 2 != 0:
            canvas.create_rectangle((past[0], past[1]), (past[0]+74, past[1]+74), fill='#7F705D')
            if j < 5:
                canvas.create_oval((past[0], past[1]), (past[0]+74, past[1]+74), fill='#000')
            past[0], past[1] = past[0]+74, past[1]
        canvas.create_rectangle((past[0], past[1]), (past[0]+74, past[1]+74))
        past[0], past[1] = past[0]+74, past[1]
        if j % 2 == 0:
            canvas.create_rectangle((past[0], past[1]), (past[0]+74, past[1]+74), fill='#7F705D')
            if j < 5:
                canvas.create_oval((past[0], past[1]), (past[0]+74, past[1]+74), fill='#000')
            past[0], past[1] = past[0]+74, past[1]        
        
    past = [2, past[1]+74]
canvas.pack()
main.mainloop()