from services import admin_service
def MostrarRanking():
    dados = admin_service.RankingGeralCalculo()
    if dados:
        print("🏆 Ranking Geral de Usuários")
        for pos, (user, streak) in enumerate(dados, start=1):
            print(f"{pos}º - Usuário: {user} | Streak: {streak}")
    else:
        print("Nenhum dado encontrado!")
def MostrarTaxa():
    taxa = admin_service.TaxaDeConclusaoCalculo()
    if taxa:
        print("📈 Taxa de Conclusão")
        for pos, (total,usuario,realizado,abandonado) in enumerate(taxa, start=1):
            print(f'''{pos}º - Usuário: {usuario} | Total de Registros: {total} |
                    Taxa de Conclusão: {((realizado/total)*100):.2f}%''')
    else:
        print("Nenhum dado encontrado!")
def MostrarHabitoConsistente():
    consistencia = admin_service.HabitoConsistente()
    if consistencia:
        print("                 🔥 Hábito Mais Consistente")
        for pos,(iduser,usuario,habito,reps) in enumerate(consistencia, start=1):
            print(f'''{pos}º - Usuário: {usuario} | Hábito: {habito} | Realizações Totais: {reps}''')
    else:
        print("Nenhum dado encontrado!")
def MostrarDiaProdutivo():
    datas = admin_service.DiaProdutivo()
    if datas:
        print("                 📅 Dias Mais Produtivos")
        for pos,(dia,reps) in enumerate(datas.items(),start=1):
            print(f'''{pos}º - Dia da Semana: {dia} | Realizações Totais: {reps["reps"]}''')
    else:
        print("Nenhum dado encontrado!")
def MostrarBaixoDesempenho():
    users = admin_service.BaixoDesempenho()
    if users:
        print("""               ⚠️ Usuários com Baixo Desempenho
        OBS: Usuários com Taxa de Conclusão menor que 60%""")
        for pos,(cont,email,reps,taxa) in enumerate (users,start=1):
            print(f"{pos}º - Usuário: {email} | Taxa de Conclusão: {taxa:.2f}%")
    else:
        print("Nenhum dado encontrado!")