

def cadastrar_usuario(usuarios):
    nome = input("Digite o seu nome: ")
    idade = input("Digite a sua idade: ")

    usuario = [nome, idade, []]

    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")


def cadastrar_vacina(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado, cadastre um primeiro.")
        return

    nome_usuario = input("Digite o nome do usuário: ")
    ususario_encontrado = False

    for usuario in usuarios:
        if usuario[0].lower() == nome_usuario.lower():
            vacina = input("Digite o nome da vacina: ")
            usuario[2].append(vacina)
            ususario_encontrado = True
            print("Vacinação cadastrada com sucesso!")

    if not ususario_encontrado:
        print("Usuário não encontrado.")


def mostrar_carteira(usuarios):
    if not usuarios:
        print('Nenhum usuário cadastrado, cadastre um primeiro: ')
        return

    nome_usuario = input('digite o nome do paciente:')
    usuario_encotrado = False
    for usuario in usuarios:
        if usuario[0].lower() == nome_usuario.lower():
            print(f'Nome: {usuario[0]}')
            print(f'idade: {usuario[1]}')
            print('Vacinas: ')
            for vacina in usuario[2]:
                print(f' - {vacina}')
            usuario_encotrado = True

    if not usuario_encotrado:
        print('Usuário não encontrado. ')


def main():
    usuarios = []

    while True:
        print('------------- Carterinha de vacinação -------------')
        print("1. Cadastrar novo Usuário")
        print("2. Cadastrar vacinação")
        print("3. Exibir carteirinha de Usuário")
        print("4. Sair")

        escolha = input("Escolha uma opção (1/2/3/4): ")

        if escolha == "1":
            cadastrar_usuario(usuarios)

        elif escolha == "2":
            cadastrar_vacina(usuarios)

        elif escolha == "3":
            mostrar_carteira(usuarios)

        elif escolha == "4":
            print("Saindo do programa. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")


main()
print('----------------------------------------------------')
