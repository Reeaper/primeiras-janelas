from tkinter import *

janela = Tk()

# funçao que é usado no botao
def click():
    tag['text']='Olá',entrada.get()
    tag['bg']='#ffa7fe'

janela.geometry('500x400+50+200')

janela.iconbitmap('icons8-capivara-48.ico')

janela.title('Capy Dev')

janela['bg']=('#ffd9ff')

tag = Label(janela,
            height=10,
            width=50,
            fg='black',
            text='Insira seu nome',
            bg='#ffb1f6',
            relief='groove')
tag.pack()

entrada=Entry(janela,width=50)
entrada.pack()
# get recebe informaçoes
# insert insere informaçoes
entrada.get()

btn=Button(janela,
           text='Enviar',
           bg='#f7b9f0',
           fg='black',
           padx=10,
           pady=3,
           command=click)
btn.pack()

janela.mainloop()