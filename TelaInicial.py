from ttkbootstrap import *
import pyperclip #pip install pyperclip
from GerarReferencia import gerarReferencia

# Função de limpar as entradas
def limpar():
    inputAutor1.delete(0, "end")
    inputTituloDoArtigo.delete(0, "end")
    inputNomeDoSite.delete(0, "end")
    inputAnoPublicacao.delete(0, "end")
    inputLink.delete(0, "end")

# Função do botão "Gerar referência"
def botaoGerarOnClick():
    # Verifica se tem texto nestes componentes e limpa-os para nova entrada
    try:
        labelReferencia.delete(0, "end")
        labelReferenciaGerada.delete(0, "end")
        labelTransferencia.delete(0, "end")
    except:
        # Componente da Referencia
        labelReferencia = Label(telaPrincipal, text="Referencia:")
        labelReferencia.grid(row= 14, column= 0, padx= 10, pady= 10, sticky="w")

    autor = inputAutor1.get()
    tituloDoArtigo = inputTituloDoArtigo.get()
    nomeDoSite = inputNomeDoSite.get()
    ano = inputAnoPublicacao.get()
    link = inputLink.get()

    print(autor, tituloDoArtigo, nomeDoSite, ano, link)

    referencia = gerarReferencia(autor, tituloDoArtigo, nomeDoSite, ano, link)

    #TODO ajustar ao tamanho do texto
    # Componente da Referencia Gerada
    labelReferenciaGerada = Label(telaPrincipal, text=referencia)
    labelReferenciaGerada.grid(row= 14, column= 1, padx= 10, pady= 10, sticky="w")

    try:
        pyperclip.copy(referencia)

        copiado = "Copiado para a Área de Transferência!"

    except:
        copiado = "Não foi possível copiar para sua área de transferência. Tente copiar manualmente."

    # TODO Arrumar para eu conseguir de fato copiar manualmente
    # Componente do aviso da cópia para a área de trasferência
    labelTransferencia = Label(telaPrincipal, text=copiado)
    labelTransferencia.grid(row= 16, column= 1, padx= 10, pady= 10, sticky="w")

    limpar()

    print("Foi chamado")

# Predefinições
telaPrincipal = Window()
telaPrincipal.geometry("700x500")
telaPrincipal.title("Gerador de Referência ABNT")
style = Style("cyborg")

# Permitir que a coluna dos Entry ocupe toda a largura disponível
telaPrincipal.grid_columnconfigure(1, weight=1)

# Título
labelTitulo = Label(telaPrincipal, text="Gerador de Referência ABNT")
labelTitulo.grid(row= 0, column= 1, padx= 10, pady= 10)

# Componentes do Título do Artigo
labelTituloDoArtigo = Label(telaPrincipal, text="Título do artigo:")
labelTituloDoArtigo.grid(row= 2, column= 0, padx= 10, pady= 10, sticky="w")
inputTituloDoArtigo = Entry(telaPrincipal)
inputTituloDoArtigo.grid(row= 2, column= 1, padx= 10, pady= 10, sticky="nsew")

# Componentes do Nome do Site
labelNomeDoSite = Label(telaPrincipal, text="Nome do site:")
labelNomeDoSite.grid(row= 4, column= 0, padx= 10, pady= 10, sticky="w")
inputNomeDoSite = Entry(telaPrincipal)
inputNomeDoSite.grid(row= 4, column= 1, padx= 10, pady= 10, sticky="nsew")

# Componentes do Ano de Publicação
labelAnoPublicacao = Label(telaPrincipal, text="Ano da publicação:")
labelAnoPublicacao.grid(row= 6, column= 0, padx= 10, pady= 10, sticky="w")
inputAnoPublicacao = Entry(telaPrincipal)
inputAnoPublicacao.grid(row= 6, column= 1, padx= 10, pady= 10, sticky="nsew")

# Componentes do Link
labelLink = Label(telaPrincipal, text="Link do artigo:")
labelLink.grid(row= 8, column= 0, padx= 10, pady= 10, sticky="w")
inputLink = Entry(telaPrincipal)
inputLink.grid(row= 8, column= 1, padx= 10, pady= 10, sticky="nsew")

# Componentes do Autor
x = 0
labelAutor1 = Label(telaPrincipal, text="Nome do autor(a):")
labelAutor1.grid(row= 10, column= 0, padx= 10, pady= 10)
inputAutor1 = Entry(telaPrincipal)
inputAutor1.grid(row= 10, column= 1, padx= 10, pady= 10, sticky="nsew")

# TODO hint de "SOBRENOME, Nome do autor"

# if(inputAutor1.cget("text") != ""):
#     x += 2

#     labelAutor2 = Label(telaPrincipal, text="Digite o nome do autor(a) (Se houver):")
#     labelAutor2.grid(row= 10 + x, column= 0, padx= 10, pady= 10)
#     inputAutor2 = Entry(telaPrincipal)
#     inputAutor2.grid(row= 10 + x, column= 1, padx= 10, pady= 10, sticky="nsew")

#     if(inputAutor2.cget("text") != ""):
#         x += 2

#         labelAutor3 = Label(telaPrincipal, text="Digite o nome do autor(a) (Se houver):")
#         labelAutor3.grid(row= 10 + x, column= 0, padx= 10, pady= 10)
#         inputAutor3 = Entry(telaPrincipal)
#         inputAutor3.grid(row= 10 + x, column= 1, padx= 10, pady= 10, sticky="nsew")

#         if(inputAutor3.cget("text") != ""):
#             x += 2

#             labelAutor4 = Label(telaPrincipal, text="Digite o nome do autor(a) (Se houver):")
#             labelAutor4.grid(row= 10 + x, column= 0, padx= 10, pady= 10)
#             inputAutor4 = Entry(telaPrincipal)
#             inputAutor4.grid(row= 10 + x, column= 1, padx= 10, pady= 10, sticky="nsew")

# Componente do Botão
botaoGerar = Button(telaPrincipal, text="Gerar referência", bootstyle = "success", command=botaoGerarOnClick)
botaoGerar.grid(row= 12 + x, column= 1, padx= 10, pady= 10)

#Chamar a Tela

telaPrincipal.mainloop()

# link = inputLink.get("1.0", END)