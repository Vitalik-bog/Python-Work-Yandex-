def move_wrap(oval):
    if canvas.coords(oval)[0] < 0:
        canvas.move(oval, 600, 0)
    elif canvas.coords(oval)[0] > 600:
        canvas.move(oval, -canvas.coords(oval)[0], 0)
    elif canvas.coords(oval)[1] > 600:
        canvas.move(oval, 0, -canvas.coords(oval)[1])
    elif canvas.coords(oval)[1] < 0:
        canvas.move(oval, 0, 600)