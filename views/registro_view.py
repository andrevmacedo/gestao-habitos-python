from services import registro_service, habito_service, usuario_service
def MenuRegistros(usuario_login):
    usuario = usuario_service.ConsultarIDEmail(usuario_login)
    while True:
        print('''
        0. Voltar ao Menu Principal
        1. Registrar execução diária
        2. Atualizar registro do dia
            ''')
        op = int(input("Indique a opção desejada: "))
        match op:
            case 0:
                return
            case 1:
                RegistrarExecucao(usuario)
            case 2:
                AtualizarRegistro(usuario)
            case _:
                print("Opção Inválida")
def MostrarNotaExecucao(dados,data):
    print(f'''
        ID do Hábito: {dados[0]}
        ID do Usuário: {dados[1]}
        Usuário: {dados[3]}
        Hábito: {dados[4]}
        Descrição: {dados[5]}
        Dificuldade: {dados[6]}
        Status: {dados[7]}
        Data de Execução: {data}
            ''')
def MostrarRegistro(dados):
    print(f'''
        ID do Registro: {dados[0]}
        ID do Hábito: {dados[1]}
        Data de Execução: {dados[2]}
        Hábito: {dados[4]}
        Descrição: {dados[5]}
        Dificuldade: {dados[6]}
        Status: {dados[7]}
            ''')
def RegistrarExecucao(usuario):
    data = registro_service.get_DataAtual()
    idhabito = int(input("Digite o ID que deseja registrar: "))
    habito = habito_service.BuscarHabito(idhabito,usuario)
    if not habito or habito[7] == "Desativado":
        print("Hábito não encontrado ou Hábito desativado!")
        return
    if registro_service.VerificarRegistro(idhabito):
        print("Hábito já registrado!")
        return
    MostrarNotaExecucao(habito,data)
    descricao = input("Descreva como foi a realização...\n")
    if ConfirmarExecucao():
        print(registro_service.Registrar(idhabito,usuario,descricao))
    else:
        print("Operação Interrompida!")
        return
def ConfirmarExecucao():
    op = int(input('''
        Deseja confirmar o registro?
        1. Sim
        2. Não
        Indique a opção desejada: '''))
    match op:
        case 1:
            return True
        case 2:
            return False
        case _:
            return False
def AtualizarRegistro(usuario):
    idhabito = input("""
        OBS: *Você apenas pode alterar hábitos 
            não realizados no dia anterior!*
        Digite o ID do Hábito que deseja alterar: """)
    dados = registro_service.ConsultarNRealizados(idhabito)
    if not dados:
        print("Hábito já registrado!")
        return
    MostrarRegistro(dados)
    descricao = input('''Descrição...
    ''')
    print(registro_service.AlterarRegistro(usuario,idhabito,descricao))
    