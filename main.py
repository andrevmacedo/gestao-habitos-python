from models import usuario
from models import habitos
from models import registros
from models import consultas_user
from models import consultas_admin
from tests import test_conexao
from database.conexao import db
test_conexao.testar_conexao()
# def Menu():
#     while True:
#         usuario_login = usuario.Usuario.usuario_logado
#         if usuario_login is not None and usuario_login != "admin@":
#             MenuLogado(usuario_login,db)
#         elif usuario_login == "admin@":
#             MenuAdmin(db)
#         else:
#             if not MenuSemLogin():
#                 break

# def MenuLogado(usuario_login,db):
#         usuarioo = db.ConsultarIDLogin(usuario_login)
#         registros.HabitosNaoConcluidos(db,usuarioo)
#         busca = consultas_user.AtualizarStreakUsuario(db,usuarioo)
#         if busca:
#             registro, _, _, _, _ = busca
#             db.AtualizarStreakUnico(registro)
#         else:
#             pass
#         print('''
#             ╔══════════════════════════════════════════════╗
#             ║  Bem-vindo ao Sistema de Gestão de Hábitos   ║
#             ╚══════════════════════════════════════════════╝
#               2. Consultar Perfil ✅
#               3. Gestão de Hábitos ✅
#               4. Registro de Execução ✅
#               0. Logout ✅
#               ''')
#         op = int(input("Indique a opção desejada: "))
#         match op:
#             case 0:
#                 usuario.Usuario.LogoutSistema()
#             case 2:
#                 consultas_user.Main(db,usuario_login)
#             case 3:
#                 habitos.Main(db,usuario_login)
#             case 4:
#                 registros.Main(db,usuario_login)
#             case _:
#                 print("Opção Inválida!")
# def MenuSemLogin():
#     print('''
#             ╔══════════════════════════════════════════════╗
#             ║  Bem-vindo ao Sistema de Gestão de Hábitos   ║
#             ╚══════════════════════════════════════════════╝
#               1. Acessar Sistema ✅
#               2. Sair ✅
#               ''')
#     op = int(input("Indique a opção desejada: "))
#     match op:
#         case 1:
#             usuario.Main(db)
#             return True
#         case 2:
#             return False
#         case _:
#             print("Opção Inválida!")
# def MenuAdmin(db):
#     print('''
#         ╔══════════════════════════════╗
#         ║   Bem-vindo Administrador!   ║
#         ╚══════════════════════════════╝
#             0. Sair
#             1. Ranking geral de usuários
#             2. Taxa de conclusão por usuário
#             3. Hábito mais consistente por usuário
#             4. Dias mais produtivos da semana
#             5. Usuários com baixo desempenho
#           ''')
#     op = int(input("Indique a opção desejada: "))
#     match op:
#         case 0:
#             usuario.Usuario.LogoutSistema()
#         case 1:
#             dados = consultas_admin.RankingGeralCalculo(db)
#             consultas_admin.MostrarRanking(dados)
#         case 2:
#             taxa = consultas_admin.TaxaDeConclusaoCalculo(db)
#             consultas_admin.MostrarTaxa(taxa)
#         case 3:
#             consistencia = consultas_admin.HabitoConsistente(db)
#             consultas_admin.MostrarHabitoConsistente(consistencia)
#         case 4:
#             datas = consultas_admin.DiaProdutivo(db)
#             consultas_admin.MostrarDiaProdutivo(datas)
#         case 5:
#             users = consultas_admin.UsuariosBaixoDesempenho(db)
#             consultas_admin.MostrarBaixoDesempenho(users)
#         case _:
#             print("Opção Inválida!")
# def Main():
#     Menu()
# Main()