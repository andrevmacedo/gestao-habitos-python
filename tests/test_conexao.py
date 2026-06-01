from database.conexao import db
def testar_conexao():
    db.cursor.execute("select 1")
    return db.cursor.fetchone()
if testar_conexao():
    print("Conexão OK!")
else:
    print("Erro ao conectar!")