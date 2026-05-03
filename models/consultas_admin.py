from datetime import datetime
def RankingGeralCalculo(db):
    return db.RankingGeral()
def MostrarRanking(dados):
    if dados:
        print("🏆 Ranking Geral de Usuários")
        for pos, (user, streak) in enumerate(dados, start=1):
            print(f"{pos}º - Usuário: {user} | Streak: {streak}")
    else:
        print("Nenhum dado encontrado!")
def TaxaDeConclusaoCalculo(db):
    return db.TaxaDeConclusao()
def MostrarTaxa(taxa):
    if taxa:
        print("📈 Taxa de Conclusão")
        for pos, (total,usuario,realizado,abandonado) in enumerate(taxa, start=1):
            print(f'''{pos}º - Usuário: {usuario} | Total de Registros: {total} |
                    Taxa de Conclusão: {((realizado/total)*100):.2f}%''')
    else:
        print("Nenhum dado encontrado!")
def HabitoConsistente(db):
    return db.HabitosMaisConsistentes()
def MostrarHabitoConsistente(consistencia):
    if consistencia:
        print("                 🔥 Hábito Mais Consistente")
        for pos,(iduser,usuario,habito,reps) in enumerate(consistencia, start=1):
            print(f'''{pos}º - Usuário: {usuario} | Hábito: {habito} | Realizações Totais: {reps}''')
    else:
        print("Nenhum dado encontrado!")
def DiaProdutivo(db):
    data_formatada = []
    diasprodutivos = {}
    dados = db.DiasMaisProdutivos()
    for data, reps in dados:
        data_formatada.append(datetime.strptime(data, "%Y-%m-%d"))
    for datas, (data, reps) in zip (data_formatada, dados):
        diasprodutivos[datas.strftime("%A")] = {"reps":reps}
    return diasprodutivos
def MostrarDiaProdutivo(datas):
    if datas:
        print("                 📅 Dias Mais Produtivos")
        for pos,(dia,reps) in enumerate(datas.items(),start=1):
            print(f'''{pos}º - Dia da Semana: {dia} | Realizações Totais: {reps["reps"]}''')
    else:
        print("Nenhum dado encontrado!")
def UsuariosBaixoDesempenho(db):
    return db.UsuariosBaixoDesempenho()
def MostrarBaixoDesempenho(users):
    if users:
        print("""               ⚠️ Usuários com Baixo Desempenho
        OBS: Usuários com Taxa de Conclusão menor que 60%""")
        for pos,(cont,email,reps,taxa) in enumerate (users,start=1):
            print(f"{pos}º - Usuário: {email} | Taxa de Conclusão: {taxa:.2f}%")
    else:
        print("Nenhum dado encontrado!")