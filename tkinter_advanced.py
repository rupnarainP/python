import tkinter
import os

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

mainWindow = tkinter.Tk()
mainWindow.title('GRID DEMO')
mainWindow.geometry('640x480+500+300')# the last 2 values are the offset from the screen border(+ is from the left and down, and - is from the right and up)

label = tkinter.Label(mainWindow, text='TKinter Grid Demo')
label.grid(row=0, column=0, columnspan=3)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

file_List = tkinter.Listbox(mainWindow)
file_List.grid(row=1, column=0, sticky='nsew', rowspan=2)
file_List.config(border=2, relief='sunken')

# for zone in os.listdir('usr/bin'): #to use in linux

for zone in os.listdir('windows/System32'):
    print()

mainWindow.mainloop()