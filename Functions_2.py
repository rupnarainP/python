import tkinter


def parabola(x):
    y = x * x / 100

    return y


def draw_axis(canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill='black')
    canvas.create_line(0, y_origin, 0, -y_origin, fill='black')


def plot(canvas, x, y):
    canvas.create_line(x, y, x + 1, y + 1, fill='red')


mainWindow = tkinter.Tk()
mainWindow.title('Parabola')
mainWindow.geometry('1920x1080')

canvas = tkinter.Canvas(mainWindow, width=1920/2, height=1080/2)
canvas.grid(row=0, column=0)

canvas2 = tkinter.Canvas(mainWindow, width=1920/2, height=1080/2)
canvas2.grid(row=0, column=1)

draw_axis(canvas)
draw_axis(canvas2)

for x in range(-100, 100):
    y = parabola(x)
    plot(canvas, x, -y)


mainWindow.mainloop()
