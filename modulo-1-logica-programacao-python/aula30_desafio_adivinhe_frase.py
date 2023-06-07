"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
# for letra in texto
palavra_secreta = 'abajur'
palavras_acertadas = ''
continuar = True
inicio = None

while continuar :

    letra = input('Digite uma letra: ')

    if letra in palavra_secreta :

        palavras_acertadas += letra


    if palavra_secreta == palavras_acertadas:
        print(f'Parabéns você acertou: {palavra_secreta}')
        break
    else:
        print(f'A palavra secreta é: {palavras_acertadas}')

    sair = input('Deseja continuar o jogo? [s] ou [n] ').lower()

    if (sair == 'n'):
        continuar = False
        print('Game Over!')


