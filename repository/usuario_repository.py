from database.conexao import db
def ConfirmarEmail(email):
    db.cursor.execute('''
                    select * from usuarios where email = ?
                        ''',(email,))
    return db.cursor.fetchone()
def CadastrarUsuarioBanco(usuario):
    db.cursor.execute('''
                    insert into usuarios values (?,?,?,?,?)
                        ''', (None,usuario._nome,usuario._email,usuario._senha,1))
    db.commit()
    return db.cursor.lastrowid #RETORNA ÚLTIMO ID CRIADO
def VerificarLogin(email,senha):
    db.cursor.execute('''
                    select * from usuarios where email = ? and senha = ? and status = 1
                        ''',(email,senha))
    return db.cursor.fetchone()
def ConsultarIDLogin(usuario):
    db.cursor.execute("select id_usuario from usuarios where email = ?",(usuario,))
    return db.cursor.fetchone()