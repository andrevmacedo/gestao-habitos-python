from models.registros import Registros
from datetime import datetime
class Streak:
    def __init__(self,idusuario,streakatual,melhorstreak):
        self._idusuario = idusuario
        self._streakatual = streakatual
        self._melhorstreak = melhorstreak
    @classmethod
    def CalcularSteakGeral(cls,steakgeneral):
        data_formatada = []
        steak = []
        for x, in steakgeneral:
            data_formatada.append(datetime.strptime(x, "%Y-%m-%d").date())
        for y in range(len(data_formatada) - 1):
            atual = data_formatada[y]
            proxima = data_formatada[y + 1]
            if (atual - proxima).days == 1:
                steak.append(atual)
            else:
                break
        return len(steak)
    @classmethod
    def SequenciaPorHabito(cls,steakporhabito):
        data_formatada = []
        steak = []
        idhabito_lista = []
        datas_lista = []
        steakmaishabito = {}
        for datas,idhabito, in steakporhabito:
            idhabito_lista.append(idhabito)
            datas_lista.append(datas.split(','))
        for listas in datas_lista:
            sublista = []
            for datas in listas:
                sublista.append(datetime.strptime(datas, "%Y-%m-%d").date())
            data_formatada.append(sublista)
        for listas in data_formatada:
            listas.sort()
            if not listas:
                steak.append(0)
                continue
            ultima = listas[-1]
            if (Registros.hoje - ultima).days > 1:
                steak.append(0)
                continue
            cont = 0
            for y in range(len(listas) - 1, 0, -1):  
                atual = listas[y]
                anterior = listas[y - 1]
                if (atual - anterior).days == 1:
                    cont += 1
                else:
                    break
            steak.append(cont)
        for habito, contador in zip(idhabito_lista, steak):
            steakmaishabito[habito] = {"steak": contador}
        return steakmaishabito
def RegistrarHabitosSeparados(db,usuario,streakporhabito):
    dados = []
    registrar = []
    atualizar = []
    for habito in streakporhabito.keys():
        dados.append(habito)
    idhabito = db.BuscarIDHabitosSequencia(dados)
    for (idh), (habito, sequencia) in zip(idhabito, streakporhabito.items()):
        registrar.append((None,usuario[0],idh[0],sequencia['steak'],sequencia['steak']))
        atualizar.append((sequencia['steak'],sequencia['steak'],usuario[0],idh[0]))
    db.RegistrarStreakHabitos(registrar)
    db.AtualizarStreakHabitos(atualizar)
def AtualizarStreakUsuario(db,usuario):
    steakgeneral = db.SteakAtual(usuario)
    if not steakgeneral:
        return None
    steakporhabito = db.SteakPorHabito(usuario)
    streak,streakporhabito = Streak.CalcularSteakGeral(steakgeneral), Streak.SequenciaPorHabito(steakporhabito)
    RegistrarHabitosSeparados(db,usuario,streakporhabito)
    registro = Streak(usuario[0],streak,streak)
    db.RegistrarStreakUnico(registro)
    melhorsteak = db.BuscarMelhorStreak(usuario)
    return registro,steakgeneral,streak,streakporhabito,melhorsteak

