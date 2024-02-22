from tkinter import *

janela = Tk()

janela.geometry('500x400+50+200')

janela.iconbitmap('icons8-capivara-48.ico')

janela.title('Capy Dev')

janela['bg']=('#ffd9ff')

tag = Label(janela,
            height=5,
            width=25,
            fg='black',
            text='Insira seu nome',
            bg='#ffb1f6',
            relief='groove',
            font=16)
tag.pack()

entrada=Entry(janela,width=50)
entrada.pack()
entrada.get()

btn=Button(janela,
           text='Fechar',
           font=10,
           padx='5',
           pady='3',
           command=janela.quit)
btn.pack()


janela.mainloop()