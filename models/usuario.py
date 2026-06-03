class Usuario:
    usuario_logado = None
    def __init__(self,nome,email,senha):
        self._nome = nome
        self._email = email
        self._senha = senha
    # staticmethod — não precisa de nada da classe
    @staticmethod
    def ConfirmarSenha(senha,confirm):
        return senha == confirm
        # A comparação já retorna True/False
    @staticmethod
    def VerificarEmail(email):
        return "@" in email
    @classmethod
    def LoginSistema(cls,usuario):
        cls.usuario_logado = usuario
    @classmethod
    def LogoutSistema(cls):
        cls.usuario_logado = None

