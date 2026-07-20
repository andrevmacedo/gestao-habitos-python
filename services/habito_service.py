from models.habitos import Habitos
from repository.habito_repository import HabitoRepository
from database.conexao import db
repo_habito = HabitoRepository(db)
def Cadastrar(nome,descricao,dificuldade,usuario):
    habito = Habitos(nome,descricao,Habitos.definir_dificuldade(dificuldade))
    if repo_habito.CriarHabito(habito,usuario):
        return "Hábito Cadastrado!"
    else:
        return "Erro ao cadastrar Hábito!"
def BuscarHabito(idhabito,usuario):
    dados = repo_habito.ConsultarHabito(idhabito,usuario)
    if dados:
        return dados
    else:
        return None
def VerificarDificuldade(dados,alterar):
    if dados[6] == alterar:
        return None
    else:
        return Habitos.definir_dificuldade(alterar)
def EditarHabito(coluna,alterar,idhabito):
    if repo_habito.AlterarHabito(coluna,alterar,idhabito) == True:
        return "Alteração realizada com sucesso!"
    else:
        return "Erro ao realizar alteração!"
def Excluir(idhabito):
    repo_habito.ExcluirHabito(idhabito)
    return "Hábito excluído com Sucesso!"
def AlterarStatus(idhabito):
    repo_habito.AlterarStatusHabito(idhabito)
    return "Status alterado com Sucesso!"
def Listar(usuario):
    return repo_habito.ConsultarTodosHabitos(usuario)