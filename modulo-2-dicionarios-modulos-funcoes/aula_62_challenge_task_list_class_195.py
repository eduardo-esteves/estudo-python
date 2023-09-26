import json

# Aula 195

# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']


def read_task(tasks, path_file):
    data = []
    try:
        with open(path_file, 'r', encoding='utf8') as my_file:
            data = json.load(my_file)
    except FileNotFoundError:
        print('Arquivo não existe')
        save_task(tasks, path_file)
    return data


def save_task(tasks, path_file):
    data = tasks
    with open(path_file, 'w', encoding='utf8') as my_file:
        data = json.dump(tasks, my_file, ident=2, ensure_ascii=False)
    return data


PATH_FILES = 'aula_62.json'

tarefas = read_task([], PATH_FILES)
tarefas_refazer = []

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t {tarefa}')


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()

    if not tarefa:
        print('Você não digitou uma tarefa.')
        return

    tarefas.append(tarefa)
    print(f'{tarefa=} adicionada com sucesso!')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)
    print(f'{tarefa=} desfeita com sucesso!')
    print()


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
    print(f'{tarefa=} refeita com sucesso!')
    print()


tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
