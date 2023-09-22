# Aula 186, 187, 188

###################         Criando arquivos com Python + Context Manager with     #########################
#
# Usamos a função open para abrir um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
#
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)

texto_grande = [
    'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960 s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum \n',
    'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.\n',
]

try:
    path_file = 'aula_55.txt'
    arquivo = open(path_file, 'w+', encoding='utf8')

    # write('string') para escrever linha a linha
    arquivo.write('Olá uma simples linha \n')
    arquivo.write('Essa seria uma segunda linha\n')

    # writelines(iterator) para escrever cada valor do iterator
    arquivo.writelines(texto_grande)

    # seek() para mover o ponteiro para o eixo (0,0) inicio do arquivo assim permite a leitura novamente.
    arquivo.seek(0, 0)

    print(arquivo.read())

    print()
    print('#' * 100)
    print()
except NameError as error:
     print("Houve um erro: ", error)
finally:
    arquivo.close()


# Uma alternativa a estrutura try, except e finally seria usar with open assim além de abrir o
# arquivo, a própria função vai se encarregar de fechar o arquivo no final da operação.
with open(path_file, 'a+', encoding='utf8') as arquivo:
    # print(arquivo.read())
    arquivo.write('Essa linha foi inserida no final do arquivo porque usei o modo a (apped)\nPorque se fosse com o modo w+ teria apagado todas as linhas do arquivo e teria escrito em seu inicio')
    arquivo.seek(0, 0)
    print(arquivo.read())
