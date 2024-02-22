from tkinter import *

# abre a janela
janela = Tk()

# muda o titulo
janela.title('Capybara')

# muda o icone
janela.iconbitmap('icons8-capivara-48.ico')

# muda o background color
janela['bg']=('#1d1160')

# geometry lxa+e+t => largura x altura + margem esquerda + margem topo
janela.geometry('500x500+0+50')

# mostra texto ou imagem
tag=Label(janela,text='Eu vou tomar um tacácá')
tag.pack()

# mostra texto ou imagem, define o tamanho da label(height/width) e muda o cursor
etiqueta=Label(janela,height=20,width=80,text='dançar,curtir ficar de boa. E quando chego no pará',cursor='dot')
etiqueta.pack()

# fg muda a cor do texto, bg muda o background color da label,relief  adiciona borda na label
tag_cor=Label(janela,height=20,width=80,fg='purple',bg='pink',text='Me sinto bem,o tempo voooooa',relief='groove')
tag_cor.pack()


janela.mainloop()
