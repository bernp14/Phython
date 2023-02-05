from tkinter import *

fen1 = Tk()
text1 = Label(fen1, text='Bonjour tout le monde, executez moi avec la command python -m tk !', fg='red')
text1.pack()

bou1 = Button(fen1, text='Quitter', command =fen1.destroy)
bou1.pack()
fen1.mainloop()

fen1.destroy()
