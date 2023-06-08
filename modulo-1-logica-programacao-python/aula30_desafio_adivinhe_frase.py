from typing import Union

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
palavra_secreta: str = 'abajur'
palavras_acertadas: str = ''
palavra_codificada: str = ''
continuar: bool = True
inicio: Union[None, bool] = None

while continuar:

    letra = input('Digite uma letra: ')

    if (len(letra) > 1):
        print('Só é aceito um único digito, vamos tentar novamente!')
        continue

    if letra in palavra_secreta:
        palavras_acertadas += letra if letra not in palavras_acertadas else ''

    i = 0
    for palavra in palavra_secreta:
        tem = None
        for acertada in palavras_acertadas:
            if acertada == palavra_secreta[i]:
                palavra_codificada += palavra
                tem = True
            else:
                palavra_codificada += ''
        i += 1
        palavra_codificada += '*' if tem is None else ''

    if palavra_secreta == palavra_codificada:
        print(f'Parabéns você acertou: {palavra_codificada}')
        break
    else:
        print(f'A palavra secreta é: {palavra_codificada}')

    sair = input('Deseja abandonar o jogo? [s] ou [n] ').lower()

    if sair == 's':
        continuar = False
        print('Game Over!')

    palavra_codificada = ''
