from tkinter import *

# abre a janela
janela = Tk()

# muda o titulo
janela.title('Empresa')

# muda o icone
janela.iconbitmap('icons8-capivara-48.ico')

# muda o background color
janela['bg']=('#58111A')

# geometry lxa+e+t => largura x altura + margem esquerda + margem topo
janela.geometry('500x500+0+50')

# mostra texto ou imagem
tag=Label(janela,height=5,width=80,fg='#FF00FF',bg='#58111A',text='Olá Mundo')
tag.pack()

# mostra texto ou imagem, define o tamanho da label(height/width) e muda o cursor
etiqueta=Label(janela,height=5,width=80,fg='#FF00FF',bg='#58111A',text='Olá Mundo')
etiqueta.pack()

# fg muda a cor do texto, bg muda o background color da label,relief  adiciona borda na label
tag_cor=Label(janela,height=10,width=50,fg='#FF00FF',bg='#58111A',text='Olá Mundo',relief='groove')
tag_cor.pack()


janela.mainloop()
