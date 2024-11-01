import pyperclip #pip install pyperclip
from datetime import date

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

            print("\nMais de três autores detectados!")

            break
    except:
        referencia += ". "
        break

data = str(date.today().day) + " " + mes[date.today().month - 1] + " " + str(date.today().year)

# Criando a referência perfeita
referencia += tituloDoSite + ". " + nomeDoSite + ", " + ano + ". " + "Disponível em: " + link + ". Acesso em: " + data

# Saída dos dados
if(cont < 3):
    print("")

print("\n", referencia, sep="")

try:
    pyperclip.copy(referencia)

    print("\nCopiado para a Área de Transferência!")

except:
    print("\nNão foi possível copiar para sua área de transferência. Tente copiar manualmente.")

input("\nPressione ENTER para fechar...")