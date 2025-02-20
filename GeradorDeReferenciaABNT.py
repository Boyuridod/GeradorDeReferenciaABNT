from ttkbootstrap import *

telaPrincipal = Window()

# Predefinições

telaPrincipal.geometry("700x700")
telaPrincipal.title("Gerador de Referência ABNT")
style = Style("cyborg")

# Componentes

labelLink = Label(telaPrincipal, text="Digite o link do artigo:")
labelLink.grid(row= 0, column= 0, padx= 10, pady= 10)

inputLink = Text(telaPrincipal, height=1, width=10)
inputLink.grid(row= 1, column= 0, padx= 10, pady= 10)

# link = inputLink.get("1.0", END)

labelTituloDoArtigo = Label(telaPrincipal, text="Digite o título do artigo:")
labelTituloDoArtigo.grid(row= 2, column= 0, padx= 10, pady= 10)

labelNomeDoSite = Label(telaPrincipal, text="Digite o nome do site:")
labelNomeDoSite.grid(row= 4, column= 0, padx= 10, pady= 10)

labelAnoPublicacao = Label(telaPrincipal, text="Digite o ano da publicação:")
labelAnoPublicacao.grid(row= 6, column= 0, padx= 10, pady= 10)

labelAutor = Label(telaPrincipal, text="Digite o nome do autor:")
labelAutor.grid(row= 8, column= 0, padx= 10, pady= 10)

botaoGerar = Button(telaPrincipal, text="Gerar referência", bootstyle = "success", command={print("Não implementado")})
botaoGerar.grid(row= 10, column= 0, padx= 10, pady= 10)

#Chamar a Tela

telaPrincipal.mainloop()