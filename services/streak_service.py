from datetime import datetime
from models.streak import Streak
from models.registros import Registros
from repository.streak_repository import StreakRepository
from repository.registro_repository import RegistroRepository
from repository.habito_repository import HabitoRepository
from database.conexao import db
repo_streak = StreakRepository(db)
repo_registro = RegistroRepository(db)
repo_habito = HabitoRepository(db)
def CalcularStreakGeral(datas_banco):
    """
    Recebe lista de datas do banco e calcula quantos dias
    consecutivos o usuário completou hábitos até hoje.
    Para quando encontra um dia sem sequência.
    """
    datas = [datetime.strptime(x, "%Y-%m-%d").date() for x, in datas_banco]
    streak = sum(
        1 for i in range(len(datas) - 1)
        if (datas[i] - datas[i + 1]).days == 1
    )
    return streak
def CalcularStreakPorHabito(dados_banco):
    """
    Recebe lista de (datas_concatenadas, nome_habito) do banco.
    Para cada hábito, calcula a sequência de dias consecutivos
    contando de trás para frente a partir da data mais recente.
    Retorna dicionário: { nome_habito: { 'streak': N } }
    """
    resultado = {}
    for datas_str, nome in dados_banco:
        datas = sorted([
            datetime.strptime(d, "%Y-%m-%d").date()
            for d in datas_str.split(",")
        ])
        # se não tem datas ou última data foi há mais de 1 dia, streak é 0
        if not datas or (Registros.hoje - datas[-1]).days > 1:
            resultado[nome] = {"streak": 0}
            continue
        cont = 0
        for i in range(len(datas) - 1, 0, -1):
            if (datas[i] - datas[i - 1]).days == 1:
                cont += 1
            else:
                break
        resultado[nome] = {"streak": cont}
    return resultado
def RegistrarStreakPorHabito(usuario, streak_por_habito):
    """
    Recebe o dicionário de streak por hábito e persiste no banco.
    Busca os IDs dos hábitos pelo nome, depois monta as listas
    de insert e update e envia de uma vez com executemany.
    """
    nomes = list(streak_por_habito.keys())
    ids_habitos = repo_habito.BuscarIDHabitosSequencia(nomes)
    registrar = [
        (None, usuario[0], idh[0], seq["streak"], seq["streak"])
        for idh, (_, seq) in zip(ids_habitos, streak_por_habito.items())
    ]
    atualizar = [
        (seq["streak"], seq["streak"], usuario[0], idh[0])
        for idh, (_, seq) in zip(ids_habitos, streak_por_habito.items())
    ]
    repo_streak.RegistrarStreakHabitos(registrar)
    repo_streak.AtualizarStreakHabitos(atualizar)
def AtualizarStreakUsuario(usuario):
    """
    Fluxo principal chamado ao logar:
    1. Busca datas de registros concluídos do usuário
    2. Calcula streak geral e por hábito
    3. Persiste streak por hábito
    4. Registra/atualiza streak geral
    5. Retorna os dados para a view exibir se necessário
    """
    datas_banco = repo_registro.StreakAtual(usuario)
    if not datas_banco:
        return None
    dados_por_habito = repo_registro.StreakPorHabito(usuario)
    streak_geral = CalcularStreakGeral(datas_banco)
    streak_por_habito = CalcularStreakPorHabito(dados_por_habito)
    RegistrarStreakPorHabito(usuario, streak_por_habito)
    registro = Streak(usuario[0], streak_geral, streak_geral)
    repo_streak.RegistrarStreakUnico(registro)
    melhor_streak = repo_streak.BuscarMelhorStreak(usuario)
    return registro, datas_banco, streak_geral, streak_por_habito, melhor_streak
