import tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

mainWindow = tkinter.Tk()
mainWindow.title('Hello World')
mainWindow.geometry('640x480+500+300')# the last 2 values are the offset from the screen border(+ is from the left and down, and - is from the right and up)

label = tkinter.Label(mainWindow, text='Hello World')
label.pack(side='top')

left_Frame = tkinter.Frame(mainWindow)
left_Frame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(left_Frame, relief='raised', borderwidth=1)
#canvas.pack(side='left', fill=tkinter.Y)#splits the window
#canvas.pack(side='left', fill=tkinter.X, expand=True)#have to use expand variable to split horizontally
canvas.pack(side='left', anchor='n')

right_Frame = tkinter.Frame(mainWindow)
right_Frame.pack(side='right', anchor='n', expand=True)

button1 = tkinter.Button(right_Frame, text='button1')
button2 = tkinter.Button(right_Frame, text='button2')
button3 = tkinter.Button(right_Frame, text='button3')
button1.pack(side='left')
button2.pack(side='left')
button3.pack(side='left')

mainWindow.mainloop()
