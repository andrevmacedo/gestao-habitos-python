from datetime import datetime
from repository.streak_repository import StreakRepository
from repository.registro_repository import RegistroRepository
from database.conexao import db
repo_streak = StreakRepository(db)
repo_registro = RegistroRepository(db)
def RankingGeralCalculo():
    return repo_streak.RankingGeral()
def HabitoConsistente():
    return repo_registro.HabitosMaisConsistentes()
def TaxaDeConclusaoCalculo():
    return repo_registro.TaxaDeConclusao()
def DiaProdutivo():
    dados = repo_registro.DiasMaisProdutivos()
    resultado = {}
    for data, reps in dados:
        dia_semana = datetime.strptime(data, "%Y-%m-%d").strftime("%A")
        resultado[dia_semana] = {"reps": reps}
    return resultado
def BaixoDesempenho():
    return repo_registro.UsuariosBaixoDesempenho()