from tkinter import *
# abre a janela
janela = Tk()

def clickGato():
    tag['text']='Gato Gato'
def clickNome():
    tag['text']='Akira Yuki'

# muda o titulo
janela.title('Capybara')

# muda o icone
janela.iconbitmap('icons8-capivara-48.ico')

# muda o background color
janela['bg']=('#58111A')

# geometry lxa+e+t => largura x altura + margem esquerda + margem topo
janela.geometry('500x500+0+50')

# mostra texto ou imagem
tag=Label(janela,height=5,width=80,fg='#FF00FF',bg='#58111A',text='Olá Mundo')
tag.pack()

# cria um botao(precisa do nome_da_variavel.pack() para funcionar,assim como na label)
btn=Button(janela,text='Aperte para ver um gato',bg='purple',fg='#FF00FF',padx='10',pady='30',command=clickGato)
btn.pack()

botao=Button(janela,text='Aperte para ver um nome',bg='violet',fg='white',padx='10',pady='30',command=clickNome)
botao.pack()

janela.mainloop()
