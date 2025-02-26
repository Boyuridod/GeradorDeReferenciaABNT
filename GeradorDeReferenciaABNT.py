from ttkbootstrap import *
import GerarReferencia

telaPrincipal = Window()

# Predefinições

telaPrincipal.geometry("700x500")
telaPrincipal.title("Gerador de Referência ABNT")
style = Style("cyborg")

# 🔹 Permitir que a coluna dos Entry ocupe toda a largura disponível
telaPrincipal.grid_columnconfigure(1, weight=1)

# Título

labelLink = Label(telaPrincipal, text="Gerador de Referência ABNT")
labelLink.grid(row= 0, column= 1, padx= 10, pady= 10)

# Componentes do Link

labelLink = Label(telaPrincipal, text="Digite o link do artigo:")
labelLink.grid(row= 2, column= 0, padx= 10, pady= 10, sticky="w")
inputLink = Entry(telaPrincipal)
inputLink.grid(row= 2, column= 1, padx= 10, pady= 10, sticky="nsew")

# Componentes do Título do Artigo

labelTituloDoArtigo = Label(telaPrincipal, text="Digite o título do artigo:")
labelTituloDoArtigo.grid(row= 4, column= 0, padx= 10, pady= 10, sticky="w")
inputTituloDoArtigo = Entry(telaPrincipal)
inputTituloDoArtigo.grid(row= 4, column= 1, padx= 10, pady= 10, sticky="nsew")

# Componentes do Nome do Site

labelNomeDoSite = Label(telaPrincipal, text="Digite o nome do site:")
labelNomeDoSite.grid(row= 6, column= 0, padx= 10, pady= 10, sticky="w")
inputNomeDoSite = Entry(telaPrincipal)
inputNomeDoSite.grid(row= 6, column= 1, padx= 10, pady= 10, sticky="nsew")

# Componentes do Ano de Publicação

labelAnoPublicacao = Label(telaPrincipal, text="Digite o ano da publicação:")
labelAnoPublicacao.grid(row= 8, column= 0, padx= 10, pady= 10, sticky="w")
inputAnoPublicacao = Entry(telaPrincipal)
inputAnoPublicacao.grid(row= 8, column= 1, padx= 10, pady= 10, sticky="nsew")

# Componentes do Autor

x = 0

labelAutor1 = Label(telaPrincipal, text="Digite o nome do autor(a):")
labelAutor1.grid(row= 10, column= 0, padx= 10, pady= 10)
entryAutor1 = Entry(telaPrincipal)
entryAutor1.grid(row= 10, column= 1, padx= 10, pady= 10, sticky="nsew")

if(entryAutor1.cget("text") != ""):
    x += 2

    labelAutor2 = Label(telaPrincipal, text="Digite o nome do autor(a) (Se houver):")
    labelAutor2.grid(row= 10 + x, column= 0, padx= 10, pady= 10)
    entryAutor2 = Entry(telaPrincipal)
    entryAutor2.grid(row= 10 + x, column= 1, padx= 10, pady= 10, sticky="nsew")

    if(entryAutor2.cget("text") != ""):
        x += 2

        labelAutor3 = Label(telaPrincipal, text="Digite o nome do autor(a) (Se houver):")
        labelAutor3.grid(row= 10 + x, column= 0, padx= 10, pady= 10)
        entryAutor3 = Entry(telaPrincipal)
        entryAutor3.grid(row= 10 + x, column= 1, padx= 10, pady= 10, sticky="nsew")

        if(entryAutor3.cget("text") != ""):
            x += 2

            labelAutor4 = Label(telaPrincipal, text="Digite o nome do autor(a) (Se houver):")
            labelAutor4.grid(row= 10 + x, column= 0, padx= 10, pady= 10)
            entryAutor4 = Entry(telaPrincipal)
            entryAutor4.grid(row= 10 + x, column= 1, padx= 10, pady= 10, sticky="nsew")

# Botão

botaoGerar = Button(
    telaPrincipal,
    text="Gerar referência",
    bootstyle = "success",
    command={
        print("Não implementado")
    }
)
botaoGerar.grid(row= 12 + x, column= 1, padx= 10, pady= 10)

#Chamar a Tela

telaPrincipal.mainloop()

# link = inputLink.get("1.0", END)