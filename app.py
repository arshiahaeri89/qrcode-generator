from tkinter import Tk, Label, Entry, Button, Frame
from pyqrcode import QRCode

root = Tk()
root.title('QRCode Generator')
font = ('tahoma', 20)
welcomeFrame = Frame(root)
inputFrame = Frame(root)
btnFrame = Frame(root)

def create(s=''):
    print('hi')

lblWelcome = Label(welcomeFrame, text='Type a Link and Give Your QRCode!', font=font)
lblLink = Label(inputFrame, text='Your Link: ', font=font)
entlink = Entry(inputFrame, width=25, font=font)
btnCreate = Button(btnFrame, text='Create', font=font, command=create)
btnClose = Button(btnFrame, text='Close', font=font, command=root.destroy)

lblWelcome.pack()
lblLink.pack(side='left')
entlink.pack(side='right')
btnCreate.pack(side='left', padx=10)
btnClose.pack(side='right', padx=10)

welcomeFrame.pack(padx=1, pady=1)
inputFrame.pack(padx=10, pady=10)
btnFrame.pack(padx=10, pady=10)

root.mainloop()

