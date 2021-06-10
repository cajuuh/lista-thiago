import json
import os.path
from aluno import Aluno

alunos = []
user_choice = ""
aluno = Aluno()

if os.path.isfile("lista_alunos.json"):
    aluno_from_json = Aluno()
    with open("lista_alunos.json") as dados_carregados:
        dados = json.load(dados_carregados)
        for aluno in dados:
            print(aluno)


perguntas = [
    " 1. Adicionar Aluno",
    " 2. Adicionar Nota",
    " 3. Remover Aluno",
    " 4. Remover Nota",
    " 5. Editar Nome Aluno",
    " 6. Editar Nota Aluno",
    " 7. Buscar Aluno Por Nome",
    " 8. Calcular Média da turma",
    " 9. Exibir Melhor Aluno",
    " 10. Exibir Alunos Em Ordem Alfabética",
    " 11. Exibir Aluno Por Ordenados Por Nota",
    " 12. Exibir alunos aprovados por média",
    " 13. Exibir Alunos Na Final (>=5)",
    " 14. Exibir Alunos Reprovados (<5)",
    " 15. Salva lista de alunos",
    " 16. Encerra o Programa",
]


def lista_escolhas():
    global user_choice
    for i in perguntas:
        print(i)
    user_choice = input("\n Escolha uma opção: ")


def checa_existe(lista, filtro):
    for n in lista:
        if filtro(n):
            return True
    return False


def busca_aluno(nome_aluno):
    for aluno in alunos:
        if aluno.nome == nome_aluno:
            return aluno


def do_media(notas):
    valor = 0
    for i in notas:
        if i == "":
            i = 0
        valor = valor + int(i)
    return valor / 3


def insertion_notas(lista_de_notas):
    for i in range(1, len(lista_de_notas)):
        step = lista_de_notas[i]
        j = i - 1
        while j >= 0 and step < lista_de_notas[j]:
            lista_de_notas[j + 1] = lista_de_notas[j]
            j -= 1
        lista_de_notas[j + 1] = step


def add_aluno():
    novo_aluno = Aluno()
    nome_novo_aluno = input("\n Digite o nome do novo aluno: ")
    novo_aluno.nome = nome_novo_aluno
    novo_aluno.notas = []
    novo_aluno.media = 0
    if checa_existe(alunos, lambda x: x.nome == nome_novo_aluno):
        print("Aluno já existente")
    else:
        alunos.append(novo_aluno)


def add_nota():
    nome_aluno = input("\n Digite o nome do aluno para o qual deseja adicionar uma nota: ")
    if checa_existe(alunos, lambda x: x.nome == nome_aluno):
        aluno = busca_aluno(nome_aluno)
        nova_nota1 = float(input("\n Digite a primeira nota do aluno: "))
        while nova_nota1 < 0 or nova_nota1 > 10:
            print("As notas devem estar entre 0.0 e 10.0")
            nova_nota1 = float(input("\n Digite a primeira nota do aluno: "))
        aluno.notas.append(float(nova_nota1))
        nova_nota2 = float(input("\n Digite a segunda nota do aluno: "))
        while nova_nota2 < 0 or nova_nota2 > 10:
            nova_nota2 = float(input("\n Digite a segunda nota do aluno: "))
            print("As notas devem estar entre 0.0 e 10.0")
        aluno.notas.append(float(nova_nota2))
        nova_nota3 = float(input("\n Digite a terceira nota do aluno: "))
        while nova_nota2 < 0 or nova_nota2 > 10:
            nova_nota3 = float(input("\n Digite a terceira nota do aluno: "))
            print("As notas devem estar entre 0.0 e 10.0")
        aluno.notas.append(float(nova_nota3))
        aluno.media = do_media(aluno.notas)
    else:
        print("\n Esse Aluno Não Está Cadastrado")


def remove_aluno():
    nome_aluno = input("\n Digite o nome do aluno que deseha remover: ")
    if checa_existe(alunos, lambda x: x.nome != nome_aluno):
        print("\n Esse Aluno Não Está Cadastrado")
    else:
        alunos.remove(busca_aluno(nome_aluno))


def remove_nota():
    nome_aluno = input("\n Digite o nome do aluno que deseha remover: ")
    if checa_existe(alunos, lambda x: x.nome != nome_aluno):
        print("\n Esse Aluno Não Está Cadastrado")
    else:
        nota_a_remover = input("\n Quais das notas deseja remover? 1, 2 ou 3? ")
        if nota_a_remover not in ["1", "2", "3"]:
            print("Digite notas de 1 a 3")
            remove_nota()
        else:
            aluno = busca_aluno(nome_aluno)
            if len(aluno.notas) == 0:
                print("\n Este aluno não possui notas cadastradas")
            else:
                aluno.notas.pop(int(nota_a_remover) - 1)
                aluno.media = do_media(aluno.notas)


def editar_nome_aluno():
    nome_aluno = input("\n Digite o nome do aluno que deseja editar o nome: ")
    if checa_existe(alunos, lambda x: x.nome != nome_aluno):
        print("\n Esse Aluno Não Está Cadastrado")
    else:
        novo_nome = input("\n Digite um novo nome para o aluno: ")
        aluno = busca_aluno(nome_aluno)
        aluno.nome = novo_nome


def editar_nota():
    nome_aluno = input("\n Digite o nome do aluno que deseja editar a nota: ")
    if checa_existe(alunos, lambda x: x.nome != nome_aluno):
        print("\n Esse Aluno Não Está Cadastrado")
    else:
        nota_a_remover = input("\n Quais das notas deseja editar? 1, 2 ou 3? ")
        if nota_a_remover not in ["1", "2", "3"]:
            print("Digite notas de 1 a 3")
            editar_nota()
        else:
            nova_nota = input("\n Digite a nova nota do aluno: ")
            aluno = busca_aluno(nome_aluno)
            if len(aluno.notas) == 0:
                print("\n Este aluno não possui notas cadastradas")
            else:
                aluno.notas[int(nota_a_remover) - 1] = nova_nota
                aluno.media = do_media(aluno.notas)


def busca_aluno_nome():
    nome_aluno = input("\n Digite o nome do aluno que deseja buscar: ")
    lista_alunos = []
    for aluno in alunos:
        if nome_aluno in aluno.nome:
            lista_alunos.append(aluno)

    lista_alunos.sort(key=lambda x: x.nome)
    for nomes in lista_alunos:
        if len(nomes.notas) == 0:
            print("\n" + nomes.nome + " Aluno não possui notas cadastradas. \n")
        else:
            print(
                "\n"
                + nomes.nome
                + "."
                + " Notas: "
                + str(nomes.notas[0])
                + " "
                + str(nomes.notas[1])
                + " e "
                + str(nomes.notas[2])
                + " Média: "
                + str(nomes.media)
                + "\n"
            )


def calcula_media_turma():
    media_total = 0
    for aluno in alunos:
        media_total += float(aluno.media)
    print("\n A média da turma é: " + str(media_total / len(alunos)) + "\n")


def melhor_aluno_turma():
    melhor_media = 0
    melho_aluno = Aluno()
    for aluno in alunos:
        if float(aluno.media) > melhor_media:
            melhor_media = float(aluno.media)
            melhor_aluno = aluno
    print(
        "\n"
        + melhor_aluno.nome
        + "."
        + " Notas: "
        + melhor_aluno.notas[0]
        + " "
        + melhor_aluno.notas[1]
        + " e "
        + melhor_aluno.notas[2]
        + " Média: "
        + melhor_aluno.media
        + "\n"
    )


def show_alunos_sorted_alpha():
    alunos.sort(key=lambda x: x.nome)
    for aluno in alunos:
        if len(aluno.notas) == 0:
            print("\n" + aluno.nome + " Aluno não possui notas cadastradas. \n")
        else:
            print(
                "\n"
                + aluno.nome
                + "."
                + " Notas: "
                + str(aluno.notas[0])
                + " "
                + str(aluno.notas[1])
                + " e "
                + str(aluno.notas[2])
                + " Média: "
                + str(aluno.media)
                + "\n"
            )


def show_sorted_alunos_notas():
    for aluno in alunos:
        insertion_notas(aluno.notas)
    alunos.sort(key=lambda x: x.notas[-1])
    for aluno in alunos:
        print(
            aluno.nome
            + "."
            + " Notas: "
            + str(aluno.notas[0])
            + " "
            + str(aluno.notas[1])
            + " e "
            + str(aluno.notas[2])
            + " Média: "
            + str(round(aluno.media, 1))
            + "\n"
        )


def show_alunos_by_media(case):
    lista_alunos = []
    for aluno in alunos:
        if case == "aprovados" and aluno.media >= 7:
            lista_alunos.append(aluno)
        elif case == "final" and (aluno.media >= 5 and aluno.media < 7):
            lista_alunos.append(aluno)
        elif case == "reprovados" and (aluno.meda < 5):
            lista_alunos.append(aluno)
    for aluno_aprovado in lista_alunos:
        print(
            aluno_aprovado.nome
            + "."
            + " Notas: "
            + str(aluno_aprovado.notas[0])
            + " "
            + str(aluno_aprovado.notas[1])
            + " e "
            + str(aluno_aprovado.notas[2])
            + " Média: "
            + str(round(aluno_aprovado.media, 1))
            + "\n"
        )


def save_as_json():
    lista_dumps = []
    for aluno in alunos:
        lista_dumps.append(aluno.toJson())
    with open("lista_alunos.json", "w") as escrever:
        json.dump(lista_dumps, escrever)
        print("\nSalvando...")
        print("\nLista salva com sucesso.")


while user_choice != "16":
    if user_choice == "1":
        add_aluno()
    elif user_choice == "2":
        add_nota()
    elif user_choice == "3":
        remove_aluno()
    elif user_choice == "4":
        remove_nota()
    elif user_choice == "5":
        editar_nome_aluno()
    elif user_choice == "6":
        editar_nota()
    elif user_choice == "7":
        busca_aluno_nome()
    elif user_choice == "8":
        calcula_media_turma()
    elif user_choice == "9":
        melhor_aluno_turma()
    elif user_choice == "10":
        show_alunos_sorted_alpha()
    elif user_choice == "11":
        show_sorted_alunos_notas()
    elif user_choice == "12":
        show_alunos_by_media("aprovados")
    elif user_choice == "13":
        show_alunos_by_media("final")
    elif user_choice == "14":
        show_alunos_by_media("reprovados")
    elif user_choice == "15":
        save_as_json()
    lista_escolhas()
