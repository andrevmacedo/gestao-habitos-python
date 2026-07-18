from models.registros import Registros
from repository.registro_repository import RegistroRepository
from repository.usuario_repository import UsuarioRepository
from services import habito_service
from database.conexao import db
repo_registro = RegistroRepository(db)
repo_user = UsuarioRepository(db)
def ConsultarUsuario(usuario_login):
    return repo_user.ConsultarIDEmail(usuario_login)
def ConsultarHabito(idhabito,usuario):
    return habito_service.BuscarHabito(idhabito,usuario)
def get_DataAtual():
    return Registros.get_DataFormatada()
def Registrar(idhabito,usuario,descricao):
    registro = Registros(idhabito,usuario[0],descricao,1)
    if repo_registro.CadastrarRegistro(registro):
        return "Registro Cadastrado com Sucesso!"
def VerificarRegistro(idhabito):
    return repo_registro.VerificarRegistroDiario(idhabito,Registros.get_DataFormatada())
def ConsultarNRealizados(idhabito):
    return repo_registro.ConsultarRegistroNAOFeito(idhabito,Registros.ontem)
def AlterarRegistro():
    pass