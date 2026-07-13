from models.usuario import Usuario
from repository.usuario_repository import UsuarioRepository
from database.conexao import db
repo = UsuarioRepository(db)
def Login(email,senha):
    resultado = repo.VerificarLogin(email,senha)
    if resultado: 
        Usuario.LoginSistema(email)
    return resultado
def Cadastrar(nome,email,senha,confirm):
    if not Usuario.VerificarEmail(email):
        return "Necessário '@'!"
    if not Usuario.ConfirmarSenha(senha,confirm):
        return "Senhas não Conferem!"
    if repo.VerificarEmail(email):
        return "Email já Cadastrado!"
    usuario = Usuario(nome,email,senha)
    if repo.CadastrarUsuario(usuario):
        return "Cadastro realizado com Sucesso!"
    else:
        return "Erro ao Cadastrar Usuário!"
def Logout():
    Usuario.LogoutSistema()
def ConsultarIDEmail(email):
    return repo.ConsultarIDEmail(email)
    