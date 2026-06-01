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

def MenuConsultas(db,usuario_login):
    while True:
        usuario = db.ConsultarIDLogin(usuario_login)
        print('''
            ===== MÉTRICAS DE PRODUTIVIDADE =====
                0. Voltar ao Menu Principal
                1. Ver Resumo Geral
                2. Listar Hábitos Concluídos Hoje
                3. Listar Hábitos Não Realizados Hoje
                4. Streak Atual
            =====================================
              ''')
        op = int(input("Indique a opção desejada: "))
        match op:
            case 0:
                return
            case 1:
                total = db.TotalHabitos(usuario)
                if total:
                    realizado = db.HabitosConclAband(usuario)
                    melhor = db.MelhorHabito(usuario)
                    ResumoGeral(total,realizado,melhor)
                else:
                    print("Nenhum Hábito cadastrado!")
            case 2:
                dados = db.ListarHabitosConcluidosHoje(usuario,Registros.hoje)
                if dados:
                    ListarHabitosConcluidos(dados)
                else:
                    print("Nenhum Hábito cadastrado Hoje!")
            case 3:
                dados1 = db.ListarHabitosNConcluidosHoje(usuario,Registros.hoje)
                if dados1:
                    ListarHabitosNConcluidos(dados1)
                else:
                    print("Nenhum Hábito encontrado ou TODOS Hábitos foram cadastrados Hoje!")
            case 4:
                resultado = AtualizarStreakUsuario(db,usuario)
                if resultado:
                    registro, steakgeneral, streak, streakporhabito, melhorsteak = resultado
                    if registro:
                        SteakGeral(steakgeneral,streak,streakporhabito,melhorsteak)
                else:
                    print("Nenhum Hábito encontrado!")
            case _:
                print("Opção Inválida!")
def ResumoGeral(total,realizado,melhor):
    print(f'''
                    ===== RESUMO =====
                Total de hábitos: {total[0]}
                Total de registros: {realizado[0]}
                Concluídos: {realizado[1]}
                Abandonados: {realizado[2]}
                Taxa de conclusão: {((realizado[1]/realizado[0])*100):.2f}%
                Melhor hábito: {melhor[1]}
                    ==================
    ''')
def ListarHabitosConcluidos(dados):
    for idhabito,habito,descricao,dificuldade,data,nota,status,status_texto in dados:
        print(f'''
                ID do Hábito: {idhabito}
                Hábito: {habito}
                Dificuldade: {descricao}
                Descrição do Hábito: {dificuldade}
                Data de Realização: {data}
                Descrição da Realização: {nota}
                Status: {status_texto}
              ''')
def ListarHabitosNConcluidos(dados1):
    for idhabito, habito, dificuldade, descricao in dados1: 
        print(f'''
                ID do Hábito: {idhabito}
                Hábito: {habito}
                Dificuldade: {descricao}
                Descrição do Hábito: {dificuldade}
            ''')
def SteakGeral(steakgeneral,streak,streakporhabito,melhorsteak):
    print(f'''
        ===== STREAK ATUAL =====
        
        🔥 Streak Geral: {streak} dias
        🏆 Melhor Streak Geral: {melhorsteak[0]} dias
        📅 Último dia concluído (YYYY-MM-DD): {steakgeneral[0][0]}
        
        ---------------------------------''')
    print(f'''
            📌 STREAK POR HÁBITO:''')
    for habito, sequencia in streakporhabito.items():
        print(f'''  
            🧠 {habito}: {sequencia["steak"]} dias 🔥''')
    print('''        
        ---------------------------------
        🚀 Continue assim! Você está quase batendo seu recorde!
        ---------------------------------''')
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

def Main(db,usuario_login):
    MenuConsultas(db,usuario_login)
