from ttkbootstrap import *

telaPrincipal = Window()

# Predefinições

telaPrincipal.geometry("700x500")
telaPrincipal.title("Gerador de Referência ABNT")
style = Style("cyborg")

# 🔹 Permitir que a coluna dos Entry ocupe toda a largura disponível
telaPrincipal.grid_columnconfigure(1, weight=1)

# Componentes

labelLink = Label(telaPrincipal, text="Gerador de Referência ABNT")
labelLink.grid(row= 0, column= 1, padx= 10, pady= 10)

labelLink = Label(telaPrincipal, text="Digite o link do artigo:")
labelLink.grid(row= 2, column= 0, padx= 10, pady= 10, sticky="w")
inputLink = Entry(telaPrincipal)
inputLink.grid(row= 2, column= 1, padx= 10, pady= 10, sticky="nsew")

labelTituloDoArtigo = Label(telaPrincipal, text="Digite o título do artigo:")
labelTituloDoArtigo.grid(row= 4, column= 0, padx= 10, pady= 10, sticky="w")
inputTituloDoArtigo = Entry(telaPrincipal)
inputTituloDoArtigo.grid(row= 4, column= 1, padx= 10, pady= 10, sticky="nsew")

labelNomeDoSite = Label(telaPrincipal, text="Digite o nome do site:")
labelNomeDoSite.grid(row= 6, column= 0, padx= 10, pady= 10, sticky="w")
inputNomeDoSite = Entry(telaPrincipal)
inputNomeDoSite.grid(row= 6, column= 1, padx= 10, pady= 10, sticky="nsew")

labelAnoPublicacao = Label(telaPrincipal, text="Digite o ano da publicação:")
labelAnoPublicacao.grid(row= 8, column= 0, padx= 10, pady= 10, sticky="w")
inputAnoPublicacao = Entry(telaPrincipal)
inputAnoPublicacao.grid(row= 8, column= 1, padx= 10, pady= 10, sticky="nsew")

# Autor vai ser um bagulho

labelAutor = Label(telaPrincipal, text="Digite o nome do autor:")
labelAutor.grid(row= 10, column= 0, padx= 10, pady= 10)

botaoGerar = Button(telaPrincipal, text="Gerar referência", bootstyle = "success", command={print("Não implementado")})
botaoGerar.grid(row= 12, column= 1, padx= 10, pady= 10)

#Chamar a Tela

telaPrincipal.mainloop()

# link = inputLink.get("1.0", END)