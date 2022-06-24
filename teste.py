from tkinter import *

tela = Tk()
tela.geometry('300x300')
tela.title('SISTEMINHA')

entrada = Entry(tela)
entrada.place(x=5, y=5)
botao = Button(tela)
botao.configure(text='SALVAR')
botao.place(x=30, y=30)


tela.mainloop()
