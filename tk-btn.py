from tkinter import *

def processOK():
    print("OK button clicked")

def processCancel():
    print("Cancel clicked")
window = Tk()
btnOK = Button(window, text="OK", fg="red", command=processOK)
btnCancel = Button(window, text="cancel", bg="red", command=processCancel)

btnOK.pack()
btnCancel.pack()

window.mainloop()
