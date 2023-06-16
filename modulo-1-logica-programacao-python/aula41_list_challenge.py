
import os

lista = []
continuar = True

while continuar:
    msg = 'Selecione uma opção \n[i]nserir [a]pagar [l]istar: '
    opcao = input(msg)

    try:
        if opcao == 'i':
            item = input('Valor: ')
            lista.append(item)
            os.system('clear')
        elif opcao == 'a':
            item = input('Escolha o índice para apagar: ')
            del lista[int(item)]
            os.system('clear')
        elif opcao == 'l':
            if len(lista) > 0:
                for indice, valor in enumerate(lista):
                    print(f'{indice} - {valor}')
            else:
                break
        else:
            continuar = False
    except ValueError:
        print('Error => Forneça um número válido para que o item possa ser removido')
    except IndexError:
        print('Error => Forneça um indice válido para que o item possa ser removido')
    except Exception as error:
        print(error)
