class UsuarioRepository:
    def __init__(self, db):
        self._db = db

    def VerificarEmail(self, email):
        self._db.cursor.execute(
            "select * from usuarios where email = ?",
            (email,)
        )
        return self._db.cursor.fetchone()

    def CadastrarUsuario(self, usuario):
        self._db.cursor.execute(
            "insert into usuarios values (?,?,?,?,?)",
            (None, usuario._nome, usuario._email, usuario._senha, 1)
        )
        self._db.commit()
        return self._db.cursor.lastrowid

    def VerificarLogin(self, email, senha):
        self._db.cursor.execute(
            "select * from usuarios where email = ? and senha = ? and status = 1",
            (email, senha)
        )
        return self._db.cursor.fetchone()

    def ConsultarIDEmail(self, email):
        self._db.cursor.execute(
            "select id_usuario from usuarios where email = ?",
            (email,)
        )
        return self._db.cursor.fetchone()