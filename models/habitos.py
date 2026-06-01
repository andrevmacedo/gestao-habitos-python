class Habitos:
    def __init__(self,nome,descricao,dificuldade):
        self._nome = nome
        self._descricao = descricao
        self._dificuldade = dificuldade
    @staticmethod
    def definir_dificuldade(dificuldade):
        match dificuldade:
            case 1:
                return "facil"
            case 2:
                return "medio"
            case 3:
                return "dificil"
    # @classmethod
    # def VerificarDificuldade(cls,dados,alterar):
    #     if dados[6] == alterar:
    #         return False
    #     else:
    #         return True

# def MenuHabitos(db,usuario_login):
#     while True: 
#         usuario = db.ConsultarIDLogin(usuario_login)
#         print('''
#             1. Criar Hábito
#             2. Editar Hábito
#             3. Excluir Hábito
#             4. Ativar/Desativar Hábito
#             5. Listar TODOS os Hábitos
#             0. Voltar ao Menu Principal
#               ''')
#         op = int(input("Indique a opção desejada: "))
#         match op:
#             case 0:
#                 return
#             case 1:
#                 habito = CadastrarHabito()
#                 if db.CriarHabito(habito,usuario):
#                     print("Hábito Cadastrado!")
#                 else:
#                     print("Erro ao cadastrar Hábito!")
#             case 2:
#                 resultado = EditarHabito(db,usuario)
#                 if resultado:
#                     coluna,alterar,idhabito = resultado
#                     confirm = db.AlterarHabito(coluna,alterar,idhabito)
#                     if confirm == True:
#                         print("Hábito alterado com Sucesso!")
#                     else:
#                         print(f"Erro ao alterar hábito!Erro: {confirm}")
#                 else:
#                     print("Hábito não Encontrado!")
#             case 3:
#                 idexcluir = ExcluirHabito(db,usuario)
#                 if idexcluir:
#                     db.ExcluirHabito(idexcluir)
#                     print("Hábito excluído com Sucesso!")
#                 else:
#                     print("Operação Cancelada ou ID não Encontrado!")
#             case 4:
#                 iddesativar = EditarStatusHabito(db,usuario)
#                 if iddesativar:
#                     db.AlterarStatusHabito(iddesativar)
#                     print("Status alterado com Sucesso!")
#                 else:
#                     print("Operação Cancelada ou ID não Encontrado!")
#             case 5:
#                 busca = ListarHabitos(db,usuario)
#                 if not busca:
#                     print("Erro ou Hábitos não Encontrados!")
#             case _:
#                 print("Opção Inválida!")
# def CadastrarHabito():
#     nome = input("Digite o nome do hábito: ")
#     descricao = input("Descreva...\n")
#     dificuldade = int(input('''
#                     1. Fácil
#                     2. Médio
#                     3. Difícil
#                     Indique a dificuldade: '''))
#     definicao = Habitos.DefinirDificuldade(dificuldade)
#     habito = Habitos(nome,descricao,definicao)
#     return habito
# def EditarHabito(db,usuario):
#     idhabito = int(input("Digite o ID do Hábito que deseja alterar: "))
#     dados = db.ConsultarHabtio(idhabito,usuario)
#     if dados:
#         MostrarHabito(dados)
#         coluna,dado = AlterarAtributosHabito(dados)
#         return coluna,dado,idhabito
#     else:
#         return None
# def MostrarHabito(dados):
#     print(f'''
#         ID do Hábito: {dados[0]}
#         ID do Usuário: {dados[1]}
#         Usuário: {dados[3]}
#         Hábito: {dados[4]}
#         Descrição: {dados[5]}
#         Dificuldade: {dados[6]}
#         Status: {dados[7]}
#             ''')
# def AlterarAtributosHabito(dados):
#     op = int(input('''
#             1. Hábito
#             2. Descrição
#             3. Dificuldade
#             Indique o que deseja alterar: '''))
#     match op:
#         case 1:
#             coluna = "nome"
#             alterar = input("Digite o novo nome: ")
#             return coluna,alterar
#         case 2:
#             coluna = "descricao"
#             alterar = input("Nova descrição...\n")
#             return coluna,alterar
#         case 3:
#             coluna = "dificuldade"
#             alterar = int(input('''
#             1. Fácil
#             2. Médio
#             3. Difícil
#             Indique a dificuldade: '''))
#             dificuldade = Habitos.DefinirDificuldade(alterar)
#             while not Habitos.VerificarDificuldade(dados,dificuldade):
#                 alterar = int(input('''
#             *Dificuldade semelhante a anterior!
#             1. Fácil
#             2. Médio
#             3. Difícil
#             Indique a novamente dificuldade: '''))
#                 dificuldade = Habitos.DefinirDificuldade(alterar)
#                 Habitos.VerificarDificuldade(dados,dificuldade)
#             return coluna,dificuldade
#         case _:
#             return False
# def ExcluirHabito(db,usuario):
#     idhabito = int(input("Digite o ID que deseja EXCLUIR: "))
#     dados = db.ConsultarHabtio(idhabito,usuario)
#     if dados:
#         MostrarHabito(dados)
#         if ConfirmarAlteracao():
#             return idhabito
#         else:
#             return None
#     else:
#         return None
# def ConfirmarAlteracao():
#     op = int(input('''
#         1. Sim
#         2. Não
#         Deseja alterar o estado deste hábito?
#         Indique o número da escolha: '''))
#     match op:
#         case 1:
#             return True
#         case 2:
#             return False
#         case _:
#             print("Opção Inválida!")
# def EditarStatusHabito(db,usuario):
#     idhabito = int(input("Digite o ID do Hábito que deseja DESATIVAR: "))
#     dados = db.ConsultarHabtio(idhabito,usuario)
#     if dados:
#         MostrarHabito(dados)
#         if ConfirmarAlteracao():
#             return idhabito
#         else:
#             return None
#     else:
#         return None
# def ListarHabitos(db,usuario):
#     dados = db.ConsultarTodosHabitos(usuario)
#     if dados:
#         MostrarTodosHabitos(dados)
#         return True
#     else:
#         return False
# def MostrarTodosHabitos(dados):
#     for idhabito,idusuario,idusuario2,email,nome,descricao,dificuldade,status in dados:
#         print(f'''
#         ID do Hábito: {idhabito}
#         Usuário: {email}
#         Hábito: {nome}
#         Descrição: {descricao}
#         Diculdade: {dificuldade}
#         Status: {status}
#               ''')

# def Main(db,usuario_login):
#     MenuHabitos(db,usuario_login)
    