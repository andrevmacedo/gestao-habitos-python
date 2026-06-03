from models.usuario import Usuario
from repository import usuario_repository
def Login(email,senha):
    resultado = usuario_repository.UsuarioRepository.VerificarLogin(email,senha)
    if resultado: 
        Usuario.LoginSistema(email)
    return resultado
def Cadastrar(nome,email,senha,confirm):
    if not Usuario.VerificarEmail(email):
        return "Necessário '@'!"
    if not Usuario.ConfirmarSenha(senha,confirm):
        return "Senhas não Conferem!"
    if usuario_repository.UsuarioRepository.VerificarEmail(email):
        return "Email já Cadastrado!"
    usuario = Usuario(nome,email,senha)
    if usuario_repository.UsuarioRepository.CadastrarUsuario(usuario):
        return "Cadastro Realizado com Sucesso!"
    else:
        return "Erro ao Cadastrar Usuário!"

    