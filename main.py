from services import usuario_service, registro_service, streak_service
from views import usuario_view, habito_view, consultas_view, registro_view, admin_view
from models import usuario
from tests import test_conexao

test_conexao.testar_conexao()

def Menu():
    while True:
        usuario_login = usuario.Usuario.usuario_logado
        if usuario_login == "admin@":
            MenuAdmin()
        elif usuario_login is not None:
            MenuLogado(usuario_login)
        else:
            if not usuario_view.MenuSemLogin():
                break

def MenuLogado(usuario_login):
    # roda só uma vez ao entrar no menu logado
    user = usuario_service.ConsultarIDEmail(usuario_login)
    registro_service.HabitosNaoConcluidos(user)
    streak_service.AtualizarStreakUsuario(user)

    while True:
        print('''
            ╔══════════════════════════════════════════════╗
            ║  Bem-vindo ao Sistema de Gestão de Hábitos   ║
            ╚══════════════════════════════════════════════╝
              2. Consultar Perfil
              3. Gestão de Hábitos
              4. Registro de Execução
              0. Logout
              ''')
        op = int(input("Indique a opção desejada: "))
        match op:
            case 0:
                usuario.Usuario.LogoutSistema()
                return
            case 2:
                consultas_view.MenuConsultas(usuario_login)
            case 3:
                habito_view.MenuHabitos(usuario_login)
            case 4:
                registro_view.MenuRegistros(usuario_login)
            case _:
                print("Opção Inválida!")

def MenuAdmin():
    while True:
        print('''
            ╔══════════════════════════════╗
            ║   Bem-vindo Administrador!   ║
            ╚══════════════════════════════╝
                0. Sair
                1. Ranking geral de usuários
                2. Taxa de conclusão por usuário
                3. Hábito mais consistente por usuário
                4. Dias mais produtivos da semana
                5. Usuários com baixo desempenho
              ''')
        op = int(input("Indique a opção desejada: "))
        match op:
            case 0:
                usuario.Usuario.LogoutSistema()
                return
            case 1:
                admin_view.MostrarRanking()
            case 2:
                admin_view.MostrarTaxa()
            case 3:
                admin_view.MostrarHabitoConsistente()
            case 4:
                admin_view.MostrarDiaProdutivo()
            case 5:
                admin_view.MostrarBaixoDesempenho()
            case _:
                print("Opção Inválida!")

def Main():
    Menu()

Main()