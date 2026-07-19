from models.registros import Registros
from repository.registro_repository import RegistroRepository
from database.conexao import db
repo_registro = RegistroRepository(db)
def get_DataAtual():
    return Registros.get_DataFormatada()
def Registrar(idhabito,usuario,descricao):
    registro = Registros(idhabito,usuario[0],descricao,1)
    if repo_registro.CadastrarRegistro(registro):
        return "Registro Cadastrado com Sucesso!"
def VerificarRegistro(idhabito):
    return repo_registro.VerificarRegistroDiario(idhabito,Registros.get_DataFormatada())
def ConsultarNRealizados(idhabito):
    ontem = Registros.ontem.strftime("%Y-%m-%d")
    return repo_registro.ConsultarRegistroNAOFeito(idhabito,ontem)
def AlterarRegistro(usuario,idhabito,descricao):
    ontem = Registros.ontem.strftime("%Y-%m-%d")
    if repo_registro.AlterarRegistro(usuario,idhabito,descricao,ontem):
        return "Alteração realizada com Sucesso!"
    else:
        return "Erro ao realizar alteração!"
def HabitosNaoConcluidos(usuario):
    ontem = Registros.ontem.strftime("%Y-%m-%d")
    dados = repo_registro.ConsultarHabitosNaoConcluidos(usuario,ontem)
    if not dados:
        return False
    registros = [(None, idhabito, idusuario, ontem, "Não Realizado", 0) 
                 for idusuario, idhabito in dados]
    repo_registro.RegistrarHabitosNAOFeitos(registros)
    return True
