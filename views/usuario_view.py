from models.usuario import Usuario
from services import usuario_service
import pwinput
def MenuSemLogin():
    print('''
            ╔══════════════════════════════════════════════╗
            ║  Bem-vindo ao Sistema de Gestão de Hábitos   ║
            ╚══════════════════════════════════════════════╝
              1. Acessar Sistema ✅
              2. Sair ✅
              ''')
    op = int(input("Indique a opção desejada: "))
    match op:
        case 1:
            MenuUsuario()
            return True
        case 2:
            return False
        case _:
            print("Opção Inválida!")
def MenuUsuario():
    while True:
        print('''
            1. Cadastrar Usuário
            2. Login
            0. Voltar ao Menu Principal
              ''')
        op = int(input("Indique a opção desejada: "))
        match op:
            case 0:
                return
            case 1:
                CadastroUsuario()
            case 2:
                LoginUsuario()
            case _:
                print("Opção Inválida!")
def CadastroUsuario():
    while True:
        nome = input("Digite o nome do Usuário: ")
        email = input("Digite o Email: ")
        senha = pwinput.pwinput("Digite a Senha numérica: ")
        confirm = pwinput.pwinput("Confirme sua Senha numérica: ")
        resultado = usuario_service.Cadastrar(nome,email,senha,confirm)
        print(resultado)
        if resultado == "Cadastro realizado com sucesso!":
            return

def LoginUsuario():
    usuario = input("Digite o Email do usuário: ")
    senha = pwinput.pwinput("Digite a Senha numérica: ")
    resultado = usuario_service.Login(usuario,senha)
    while not resultado:
        usuario = input("Email ou Senha Incorretos!\nDigite o Email do usuário: ")
        senha = pwinput.pwinput("Digite a Senha numérica: ")
        resultado = usuario_service.Login(usuario,senha)
    print("Login realizado com sucesso!")