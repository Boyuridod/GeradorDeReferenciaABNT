# Estrutura
## SOBRENOME, Nome do autor. Título da página ou do artigo. Nome do site, ano. Disponível em: <URL>. Acesso em: dia mês ano.

# Exemplo
## WIKIPÉDIA. Revolução Francesa. Wikipédia, 2023. Disponível em: https://pt.wikipedia.org/wiki/Revolução_Francesa. Acesso em: 06 ago. 2024.

# Mais de um autor
## Estrutura com até três autores
### SOBRENOME, Nome do autor 1; SOBRENOME, Nome do autor 2; SOBRENOME, Nome do autor 3. Título da página ou do artigo. Nome do site, ano. Disponível em: <URL>. Acesso em: dia mês ano.

## Estrutura com mais de três autores
### SOBRENOME, Nome do autor 1 et al. Título da página ou do artigo. Nome do site, ano. Disponível em: <URL>. Acesso em: dia mês ano.

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