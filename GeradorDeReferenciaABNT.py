# TODO Colocar a data automaticamente 6 ago. 2024

import pyperclip #pip install pyperclip
# import datetime

# Vetor de mêses
mes = ["Jan.", "Fev.", "Mar.", "Abr.", "Mai.", "Jun.", "Jul.", "Ago.", "Set.", "Out.", "Nov.", "Dez."]


# Recebendo as informações de entrada
link = input("Link: ")
tituloDoSite = input("Título do Artigo: ")
nomeDoSite = input("Nome do Site: ")
ano = input("Ano da publicação: ")

autor = input("SOBRENOME, Nome do autor: ")

referencia = autor

cont = 1

while(True):
    try:
        referencia += "; " + input("SOBRENOME, Nome do autor ou [Ctrl + C] para parar: ")

        cont += 1

        if(cont > 3):
            referencia = autor + " et al. "
            break
    except:
        referencia += ". "
        break

# data = str(datetime.day) + " " + mes[datetime.month] + " " + str(datetime.year)

# Criando a referência perfeita
referencia += tituloDoSite + ". " + nomeDoSite + ", " + ano + ". " + "Disponível em: " + link + ". Acesso em: " + "6 ago. 2024."

# Saída dos dados
print("\n\n", referencia, sep="")

pyperclip.copy(referencia)

print("\nCopiado para a Área de Transferência!")

# input("\nPressione ENTER para fechar...")