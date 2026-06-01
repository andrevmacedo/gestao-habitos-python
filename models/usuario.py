# import pwinput
class Usuario:
    usuario_logado = None
    def __init__(self,nome,email,senha):
        self._nome = nome
        self._email = email
        self._senha = senha
    # staticmethod — não precisa de nada da classe
    @staticmethod
    def ConfirmarSenha(senha,confirm):
        return senha == confirm
        # A comparação já retorna True/False
    @staticmethod
    def VerificarEmail(email):
        return "@" in email
    @classmethod
    def LoginSistema(cls,usuario):
        cls.usuario_logado = usuario
    @classmethod
    def LogoutSistema(cls):
        cls.usuario_logado = None

# def MenuUsuario(db):
#     while True:
#         print('''
#             1. Cadastrar Usuário
#             2. Login
#             0. Voltar ao Menu Principal
#               ''')
#         op = int(input("Indique a opção desejada: "))
#         match op:
#             case 0:
#                 return
#             case 1:
#                 usuario = CadastroUsuario(db)
#                 if usuario:
#                     banco = db.CadastrarUsuarioBanco(usuario)
#                     if banco:
#                         print("Cadastro Realizado com Sucesso!")
#                     else:
#                         print("Erro ao Cadastrar Usuário!")
#                 else:
#                     print("Email já Cadastrado!")
#             case 2:
#                 if LoginUsuario(db):
#                     print("Usuário Logado com Sucesso!")
#                 return
#             case _:
#                 print("Opção Inválida!")
# def CadastroUsuario(db):
#     nome = input("Digite o nome do Usuário: ")
#     email = input("Digite o Email: ")
#     while not Usuario.VerificarEmail(email):
#         email = input("Necessário '@'!\nDigite o Email: ")
#         Usuario.VerificarEmail(email)
#     senha = pwinput.pwinput("Digite a Senha numérica: ")
#     confirm = pwinput.pwinput("Confirme sua Senha numérica: ")
#     while not Usuario.ConfirmarSenha(senha,confirm):
#         confirm = pwinput.pwinput("Senhas não Conferem!\nConfirme sua Senha: ")
#         Usuario.ConfirmarSenha(senha,confirm)
#     if db.ConfirmarEmail(email):
#         return False
#     usuario = Usuario(nome,email,senha)
#     return usuario
# def LoginUsuario(db):
#     usuario = input("Digite o Email do usuário: ")
#     senha = pwinput.pwinput("Digite a Senha numérica: ")
#     while not db.VerificarLogin(usuario,senha):
#         usuario = input("Email ou Senha Incorretos!\nDigite o Email do usuário: ")
#         senha = pwinput.pwinput("Digite a Senha numérica: ")
#         db.VerificarLogin(usuario,senha)
#     Usuario.LoginSistema(usuario)
#     return True


# def Main(db):
#     MenuUsuario(db)