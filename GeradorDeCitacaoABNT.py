# TODO Colocar a data automaticamente 6 ago. 2024

import pyperclip #pip install pyperclip

# Recebendo as informações de entrada
link = input("Link: ")

autor = input("SOBRENOME, Nome do autor: ")

citacao = autor

cont = 1

while(True):
    try:
        citacao += "; " + input("SOBRENOME, Nome do autor ou [Ctrl + C] para parar: ")

        cont += 1

        if(cont > 3):
            citacao = autor + " et al. "
            break
    except:
        citacao += ". "
        break

tituloDoSite = input("\nTítulo do Artigo: ")
nomeDoSite = input("Nome do Site: ")
ano = input("Ano da publicação: ")

# Criando a citação perfeita
citacao += tituloDoSite + ". " + nomeDoSite + ", " + ano + ". " + "Disponível em: " + link + ". Acesso em: " + "6 ago. 2024."

# Saída dos dados
print("\n", citacao, sep="")

pyperclip.copy(citacao)

print("\nCopiado para a Área de Transferência!")

input("\nPressione ENTER para fechar...")