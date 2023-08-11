# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5x5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

index = 0
erros = 0
acertos = 0

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    count = 1

    for opcao in pergunta['Opções']:
        option = f'{count}) {opcao}'
        print(option)
        count += 1

    resposta = pergunta['Resposta']
    print()

    opcao = input('Informe a opção correta: ')

    if int(opcao) > 4:
        print('Opção inválida tente novamente')
        erros += 1
        print()
        continue

    opcao = pergunta['Opções'][(int(opcao)-1)]

    if opcao == resposta:
       print(f'Certa a resposta {opcao} 👍')
       acertos += 1
    else:
        print('Opção Incorreta')
        erros += 1

    print()
    index += 1

estatisticas = round(acertos / 3 * 100, 2)
print(f'Total acertos: {acertos}')
print(f'Total erros: {erros}')

print(f'Estatisticas: {estatisticas}% de acertos')

