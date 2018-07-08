import tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

mainWindow = tkinter.Tk()
mainWindow.title('Hello World')
mainWindow.geometry('640x480+500+300')# the last 2 values are the offset from the screen border(+ is from the left and down, and - is from the right and up)

label = tkinter.Label(mainWindow, text='Hello World')
label.grid(row=0, column=0)

left_Frame = tkinter.Frame(mainWindow)
left_Frame.grid(row=1, column=1)

canvas = tkinter.Canvas(left_Frame, relief='raised', borderwidth=1)
#canvas.pack(side='left', fill=tkinter.Y)#splits the window
#canvas.pack(side='left', fill=tkinter.X, expand=True)#have to use expand variable to split horizontally
canvas.grid(row=1, column=0)

right_Frame = tkinter.Frame(mainWindow)
right_Frame.grid(row=1, column=2, sticky='n')

button1 = tkinter.Button(right_Frame, text='button1')
button2 = tkinter.Button(right_Frame, text='button2')
button3 = tkinter.Button(right_Frame, text='button3')
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

#configure the columns
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)

left_Frame.config(relief='sunken', borderwidth=1)
right_Frame.config(relief='sunken', borderwidth=1)
left_Frame.grid(sticky='ns')
right_Frame.grid(sticky='new')

mainWindow.mainloop()
