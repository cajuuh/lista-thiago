import json
import os.path
from aluno import Aluno

opcao = input('\n.: MENU PRINCIPAL :.\n\n  1. Listar alunos\n  2. Adicionar aluno\n  3. Adicionar notas a aluno\n  4. Remover nota de um aluno\n  5. Remover aluno\n  6. Editar aluno\n  7. Editar nota aluno\n  8. Salvar Lista \n  9. Carregar Lista do Arquivo\n  10. Sair do Sistema\n\nDigite a opção desejada (1 a 7): ')

alunos = []

if os.path.isfile('lista_alunos.json'):
    with 'lista_alunos.json' as dados_carregados:
        dados = json.load(dados_carregados)
        dados.sort()
        for aluno in dados:
            alunos.append(aluno)
else:
    alunos = []

while opcao != '10':
    if opcao not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        print('\nPor favor selecione uma opção válida.\n')

    elif opcao == '1':
        print('\n********v********')
        print('\nOk. Listando os alunos...\n')

        pos = 0
        while pos < len(alunos):
            print('%d. %s' % (pos+1, alunos[pos]))
            pos += 1
        print('********v********')
    elif opcao == '2':
        aluno = Aluno()
        print('\nOk. Vamos adicionar um aluno...\n')
        nome = input('Por favor, digite o nome do aluno a adicionar: ')
        if nome == '':
            print('\nPor favor digite o nome do aluno.')

        if len(alunos) == 0:
            aluno_existe = False
        else:
            for obj in alunos:
                if obj.nome == nome:
                    aluno_existe = True
                else:
                    aluno_existe = False
        if aluno_existe == False:
            aluno.nome = nome
            alunos.append(aluno)
            print('\n Aluno adicionado')
        else:
            print('\n Aluno existe')

    elif opcao == '3':
        print('\nOk. Vamos adicionar notas a um aluno...\n')

        nome = input(
            'Por favor, digite o nome do aluno para o qual deseja adicionar notas: ')

        for aluno in alunos:
            if aluno.nome == nome:
                if len(aluno.notas) >= 3:
                    print('\nEsse aluno já possui as 3 notas.')
                else:
                    nota1 = input(
                        'Por favor, digite a primeira nota: ')
                    aluno.notas.append(nota1)
                    nota2 = input(
                        'Por favor, digite a segunda nota: ')
                    aluno.notas.append(nota2)
                    nota3 = input(
                        'Por favor, digite a terceira nota: ')
                    aluno.notas.append(nota3)
                    break
            elif aluno.nome != nome:
                print('\n Aluno não encontrado')

    elif opcao == '4':
        nome = input(
            'Por favor, digite o nome do aluno para o qual deseja remover notas: ')
        for aluno in alunos:
            if aluno.nome == nome:
                nota = input('Qual o numero da nota que voce deseja remover? ')
                if nota not in ['1', '2', '3']:
                    print('\n Nota invalida, digite de 1 a 3')
                elif nota == '1':
                    if aluno.notas[0]:
                        del aluno.notas[0]
                    else:
                        print('\n Nota não existe')
                elif nota == '2':
                    if aluno.notas[1]:
                        del aluno.notas[1]
                    else:
                        print('\n Nota não existe')
                elif nota == '3':
                    if aluno.notas[2]:
                        del aluno.notas[2]
                    else:
                        print('\n Nota não existe')
                        break
            elif aluno.nome != nome:
                print('\n Aluno não encontrado')

    elif opcao == '5':
        nome = input('Por favor, digite o nome do aluno a remover: ')
        if nome in alunos:
            alunos.remove(nome)
            with open('lista_alunos.json', 'w') as escrever:
                json.dump(alunos, escrever)
            print('\nAluno removido com sucesso.')

        else:
            print('\nAluno não encontrado.')

    elif opcao == '6':
        nome = input('Por favor, digite o nome do aluno a editar: ')
        if len(alunos):
            for aluno in alunos:
                if aluno.nome == nome:
                    novo_nome = input('Digite o novo nome do aluno: ')
                    aluno.nome = novo_nome
                    print('\n Aluno editado com sucesso.')
                    break
                else:
                    print('\n Aluno não encontrado')
        else:
            print('\n Não existem alunos cadastrados')

    elif opcao == '7':
        nome = input(
            'Por favor, digite o nome do aluno para o qual deseja editar notas: ')
        for aluno in alunos:
            if aluno.nome == nome:
                nota = input('Qual o numero da nota que voce deseja editar? ')
                if nota not in ['1', '2', '3']:
                    print('\n Nota invalida, digite de 1 a 3')
                elif nota == '1':
                    if aluno.notas[0]:
                        nova_nota1 = input('Digite a nova nota 1? ')
                        aluno.notas[0] = nova_nota1
                    else:
                        print('\n Nota não existe')
                elif nota == '2':
                    if aluno.notas[1]:
                        nova_nota2 = input('Digite a nova nota 2? ')
                        aluno.notas[1] = nova_nota2
                    else:
                        print('\n Nota não existe')
                elif nota == '3':
                    if aluno.notas[2]:
                        nova_nota3 = input('Digite a nova nota 3? ')
                        aluno.notas[2] = nova_nota3
                    else:
                        print('\n Nota não existe')
                        break
            elif aluno.nome != nome:
                print('\n Aluno não encontrado')
    elif opcao == '8':
        with open('lista_alunos.json', 'w') as escrever:
            json.dump(alunos, escrever)
            print('\nSalvando...')

            print('\nLista salva com sucesso.')

    elif opcao == '9':
        with open('lista_alunos.json') as dados_carregados:
            print('\nCarregando alunos do banco de dados...\n')

            dados = json.load(dados_carregados)
            for aluno in dados:
                print(aluno)
    opcao = input('\n.: MENU PRINCIPAL :.\n\n  1. Listar alunos\n  2. Adicionar aluno\n  3. Adicionar notas a aluno\n  4. Remover nota de um aluno\n  5. Remover aluno\n  6. Editar aluno\n  7. Editar nota aluno\n  8. Salvar Lista \n  9. Carregar Lista do Arquivo\n  10. Sair do Sistema\n\nDigite a opção desejada (1 a 7): ')

print('\nObrigado por usar o Sistema\n')
