from tkinter import Tk, Label, Entry, Button, Frame, StringVar, messagebox
from tkinter.filedialog import asksaveasfile
from pyqrcode import QRCode

root = Tk()
root.title('QRCode Generator')
font = ('tahoma', 20)
welcomeFrame = Frame(root)
inputFrame = Frame(root)
btnFrame = Frame(root)

def create(s=''):
    try:
        global linkVar
        link = linkVar.get()
        code = QRCode(link)
        file = asksaveasfile(initialfile = 'Untitled.png',
                        defaultextension=".png",
                        filetypes=[("Portable Network Graphics file (PNG)", "*.png")])
        if file:
            code.png(file.name, scale=20)
            file.close()
            messagebox.showinfo('Success', 'The QRCode Successfully Created.')
    except Exception as e:
        messagebox.showerror('Error', str(e))

linkVar = StringVar(inputFrame, '')
lblWelcome = Label(welcomeFrame, text='Type a Link and Give Your QRCode!', font=font)
lblLink = Label(inputFrame, text='Your Link: ', font=font)
entlink = Entry(inputFrame, width=25, font=font, textvariable=linkVar)
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

