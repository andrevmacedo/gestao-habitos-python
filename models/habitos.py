class Habitos:
    def __init__(self,nome,descricao,dificuldade):
        self._nome = nome
        self._descricao = descricao
        self._dificuldade = dificuldade
    @staticmethod
    def definir_dificuldade(dificuldade):
        match dificuldade:
            case 1:
                return "facil"
            case 2:
                return "medio"
            case 3:
                return "dificil"


    