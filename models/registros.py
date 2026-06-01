from datetime import date,timedelta
class Registros:
    hoje = date.today()
    ontem = hoje - timedelta(days=1)
    def __init__(self,idhabito,idusuario,descricao,status):
        self._idhabito = idhabito
        self._idusuario = idusuario
        self._data = self.hoje.strftime("%Y-%m-%d")
        self._descricao = descricao
        self._status = status
    @staticmethod
    def get_DataFormatada():
        return date.today().strftime("%Y-%m-%d")

# def MenuRegistros(db,usuario_login):
#     while True:
#         usuario = db.ConsultarIDLogin(usuario_login)
#         print('''
#         0. Voltar ao Menu Principal
#         1. Registrar execução diária
#         2. Atualizar registro do dia
#             ''')
#         op = int(input("Indique a opção desejada: "))
#         match op:
#             case 0:
#                 return
#             case 1:
#                 registro = RegistrarExecucao(db,usuario)
#                 if registro:
#                     dado = db.CadastrarRegistro(registro)
#                     if dado:
#                         print("Registro Cadastrado com Sucesso!")
#                     else:
#                         print("Erro ao Registrar Hábito!")
#                 else:
#                     print("Opção Inválida ou Hábito já cadastrado hoje!")
#             case 2:
#                 if AtualizarRegistro(db,usuario):
#                    print("Alteração realizada com Sucesso!")
#                 else:
#                     print("Registro não encontrado ou Já registrado!")
#             case _:
#                 print("Opção Inválida")
# def RegistrarExecucao(db,usuario):
#     idhabito = int(input("Digite o ID que deseja registrar: "))
#     data = Registros.get_DataFormatada()
#     if db.VerificarRegistroDiario(idhabito,data):
#         return None
#     else:
#         dados = db.ConsultarHabtio(idhabito,usuario)
#         if dados:
#             MostrarNotaExecucao(dados)
#             if dados[7] == "Desativado":
#                 return None
#             else:
#                 descricao = input("Descreva como foi a realização...\n")
#                 registro = ConfirmarExecucao(idhabito,usuario,descricao)
#                 if registro:
#                     return registro
#                 else:
#                     return None
#         else:
#             return None
# def MostrarNotaExecucao(dados):
#     print(f'''
#         ID do Hábito: {dados[0]}
#         ID do Usuário: {dados[1]}
#         Usuário: {dados[3]}
#         Hábito: {dados[4]}
#         Descrição: {dados[5]}
#         Dificuldade: {dados[6]}
#         Status: {dados[7]}
#         Data de Execução: {Registros.hoje}
#             ''')
# def ConfirmarExecucao(idhabito,usuario,descricao):
#     op = int(input('''
#         Deseja confirmar o registro?
#         1. Sim
#         2. Não
#         Indique a opção desejada: '''))
#     match op:
#         case 1:
#             registro = Registros(idhabito,usuario[0],descricao,1)
#             return registro
#         case 2:
#             return None
#         case _:
#             return None
# def HabitosNaoConcluidos(db,usuario):
#     dados = db.ConsultarHabitosNaoConcluidos(usuario,Registros.ontem)
#     if dados:
#         for idusuario,idhabito in dados:
#             db.RegistrarHabitosNAOFeitos(idhabito,idusuario,Registros.ontem)
#         return True
#     else:
#         return False
# def AtualizarRegistro(db,usuario):
#     idhabito = input("""
#         OBS: *Você apenas pode alterar hábitos 
#             não realizados no dia anterior!*
#         Digite o ID do Hábito que deseja alterar: """)
#     dados = db.ConsultarRegistroNAOFeito(idhabito,Registros.ontem)
#     if dados:
#         MostrarRegistro(dados)
#         descricao = input('''Descrição...
#         ''')
#         if db.AlterarRegistro(usuario,idhabito,descricao,Registros.ontem):
#             return True
#         else:
#             return False
#     else:
#         return False
# def MostrarRegistro(dados):
#     print(f'''
#         ID do Registro: {dados[0]}
#         ID do Hábito: {dados[1]}
#         Data de Execução: {dados[2]}
#         Hábito: {dados[4]}
#         Descrição: {dados[5]}
#         Dificuldade: {dados[6]}
#         Status: {dados[7]}
#             ''')

# def Main(db,usuario_login):
#     MenuRegistros(db,usuario_login)
