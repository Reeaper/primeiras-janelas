from tkinter import *

janela = Tk()

janela.geometry('500x400+50+200')

janela.iconbitmap('icons8-capivara-48.ico')

janela.title('Capy Dev')

janela['bg']=('#F5FFFA')

# definindo a var de soma
def click():
    # as var X e Y armazenam o valor que o usuario vai inserir
    x=entrada_num1.get()
    y=entrada_num2.get()
# if else para confirmar que os valores sao validos
    if x.isnumeric() and y.isnumeric():
    # a var Z faz a soma
        z=int(x)+int(y)
    # a var result sera chamado numa label para exibir o resultado
        result['text']=z
    else:
        result['text']="Insira apenas números inteiros!"

#titulo da entrada 
tag = Label(janela,
            height=2,
            width=20,
            fg='black',
            text='Insira o primeiro valor',
            relief='groove',
            bg='#F0FFF0')
tag.pack()

# entrada de valores
entrada_num1=Entry(janela)
entrada_num1.pack()


#titulo da entrada 
tag = Label(janela,
            height=2,
            width=20,
            fg='black',
            text='Insira o segundo valor',
            relief='groove',
            bg='#F0FFF0')
tag.pack()

# entrada de valores
entrada_num2=Entry(janela)
entrada_num2.pack()

# label que vai mostrar o resultado
result=Label(text=' ')
result.pack()

btn_soma=Button(janela,
           text='Somar',
           padx=5,
           pady=3,
           command=click)
btn_soma.pack()

btn=Button(janela,
           text='Sair',
           padx=5,
           pady=3,
           command=quit)
btn.pack()

janela.mainloop()