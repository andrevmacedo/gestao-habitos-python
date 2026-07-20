from services import streak_service, usuario_service
def MenuConsultas(usuario_login):
    usuario = usuario_service.ConsultarIDEmail(usuario_login)
    while True:
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
                resultado = streak_service.ResumoHabitos(usuario)
                if resultado:
                    total,realizado,melhor = resultado
                    ResumoGeral(total,realizado,melhor)
                else:
                    print("Nenhum Hábito cadastrado!")
            case 2:
                dados = streak_service.ListarConcluidos(usuario)
                if dados:
                    ListarHabitosConcluidos(dados)
                else:
                    print("Nenhum Hábito cadastrado Hoje!")
            case 3:
                dados1 = streak_service.ListarNConcluidos(usuario)
                if dados1:
                    ListarHabitosNConcluidos(dados1)
                else:
                    print("Nenhum Hábito encontrado ou TODOS Hábitos foram cadastrados Hoje!")
            case 4:
                resultado = streak_service.AtualizarStreakUsuario(usuario)
                if not resultado:
                    print("Nenhum Hábito encontrado!")
                else:
                    registro, streakgeneral, streak, streakporhabito, melhorstreak = resultado
                    if registro:
                        StreakGeral(streakgeneral,streak,streakporhabito,melhorstreak)
            case _:
                print("Opção Inválida!")
def ResumoGeral(total,realizado,melhor):
    if realizado[0]:
        taxa = (realizado[1] / realizado[0] * 100)
    else:
        taxa = 0
    print(f'''
                    ===== RESUMO =====
                Total de hábitos: {total[0]}
                Total de registros: {realizado[0]}
                Concluídos: {realizado[1]}
                Abandonados: {realizado[2]}
                Taxa de conclusão: {taxa:.2f}%
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
                Dificuldade: {dificuldade}
                Descrição do Hábito: {descricao}
            ''')
def StreakGeral(steakgeneral,streak,streakporhabito,melhorsteak):
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
            🧠 {habito}: {sequencia["streak"]} dias 🔥''')
    print('''        
        ---------------------------------
        🚀 Continue assim! Você está quase batendo seu recorde!
        ---------------------------------''')