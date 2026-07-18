from services import habito_service
def MenuHabitos(usuario_login):
    while True: 
        usuario = habito_service.ConsultarUsuario(usuario_login)
        print('''
            1. Criar Hábito
            2. Editar Hábito
            3. Excluir Hábito
            4. Ativar/Desativar Hábito
            5. Listar TODOS os Hábitos
            0. Voltar ao Menu Principal
              ''')
        op = int(input("Indique a opção desejada: "))
        match op:
            case 0:
                return
            case 1:
                CadastrarHabito(usuario)
            case 2:
                EditarHabito(usuario)
            case 3:
                ExcluirHabito(usuario)
            case 4:
                EditarStatusHabito(usuario)
            case 5:
                ListarHabitos(usuario)
            case _:
                print("Opção Inválida!")
def CadastrarHabito(usuario):
    nome = input("Digite o nome do hábito: ")
    descricao = input("Descreva...\n")
    dificuldade = int(input('''
                    1. Fácil
                    2. Médio
                    3. Difícil
                    Indique a dificuldade: '''))
    resultado = habito_service.Cadastrar(nome,descricao,dificuldade,usuario)
    print(resultado)
def MostrarHabito(dados):
    print(f'''
        ID do Hábito: {dados[0]}
        ID do Usuário: {dados[1]}
        Usuário: {dados[3]}
        Hábito: {dados[4]}
        Descrição: {dados[5]}
        Dificuldade: {dados[6]}
        Status: {dados[7]}
            ''')
def AlterarAtributosHabito(dados):
    op = int(input('''
            1. Hábito
            2. Descrição
            3. Dificuldade
            Indique o que deseja alterar: '''))
    match op:
        case 1:
            return "nome",input("Digite o novo nome: ")
        case 2:
            return "descricao",input("Nova descrição...\n")
        case 3:
            while True:
                alterar = int(input('''
                1. Fácil
                2. Médio
                3. Difícil
                Indique a dificuldade: '''))
                dificuldade = habito_service.VerificarDificuldade(dados,alterar)
                if dificuldade:
                    return "dificuldade",dificuldade
                print("*Dificuldade semelhante a anterior!")
        case _:
            return False
def ConfirmarAlteracao():
    op = int(input('''
        1. Sim
        2. Não
        Deseja alterar o estado deste hábito?
        Indique o número da escolha: '''))
    match op:
        case 1:
            return True
        case 2:
            return False
        case _:
            print("Opção Inválida!")
            return False 
def MostrarTodosHabitos(dados):
    for idhabito,idusuario,idusuario2,email,nome,descricao,dificuldade,status in dados:
        print(f'''
        ID do Hábito: {idhabito}
        Usuário: {email}
        Hábito: {nome}
        Descrição: {descricao}
        Diculdade: {dificuldade}
        Status: {status}
              ''')
def EditarHabito(usuario):
    idhabito = int(input("Digite o ID do Hábito que deseja alterar: "))
    dados = habito_service.BuscarHabito(idhabito,usuario)
    if not dados: 
        print("Hábito não Encontrado!")
        return
    MostrarHabito(dados)
    resultado = AlterarAtributosHabito(dados)
    if not resultado:
        print("Opção Inválida!")
    coluna, alterar = resultado
    print(habito_service.EditarHabito(coluna, alterar, idhabito))
def ExcluirHabito(usuario):
    idhabito = int(input("Digite o ID que deseja EXCLUIR: "))
    dados = habito_service.BuscarHabito(idhabito,usuario)
    if not dados:
        print("Hábito não encontrado!")
        return
    MostrarHabito(dados)
    if ConfirmarAlteracao():
        print(habito_service.Excluir(idhabito))
    else:
        print("Operação Cancelada!")
def EditarStatusHabito(usuario):
    idhabito = int(input("Digite o ID do Hábito que deseja DESATIVAR: "))
    dados = habito_service.BuscarHabito(idhabito,usuario)
    if not dados:
        print("Hábito não encontrado!")
        return
    MostrarHabito(dados)
    if ConfirmarAlteracao():
        print(habito_service.AlterarStatus(idhabito))
    else:
        print("Operação Cancelada!")
def ListarHabitos(usuario):
    dados = habito_service.Listar(usuario)
    if dados:
        MostrarTodosHabitos(dados)
    else:
        print("Erro ou Hábitos não Encontrados!")        