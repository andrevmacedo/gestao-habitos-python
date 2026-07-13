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
# def EditarHabito(db,usuario):
#     idhabito = int(input("Digite o ID do Hábito que deseja alterar: "))
#     dados = db.ConsultarHabtio(idhabito,usuario)
#     if dados:
#         MostrarHabito(dados)
#         coluna,dado = AlterarAtributosHabito(dados)
#         return coluna,dado,idhabito
#     else:
#         return None
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
# def Main(db,usuario_login):
#     MenuHabitos(db,usuario_login)
    