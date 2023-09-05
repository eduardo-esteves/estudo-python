try:
    a = 18
    b = 0
    # print(b[0])
    # print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError as error:
    # Porém alem de usar um alias e imprimir somente a mensagem de erro em "error"
    print(error)
    # Posso saber o nome da excessão também que é o nome da classe
    print(error.__class__.__name__)
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO.')
finally:
    print('CONTINUAR')
