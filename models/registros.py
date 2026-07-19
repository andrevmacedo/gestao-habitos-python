from datetime import date,timedelta
class Registros:
    hoje = date.today()
    ontem = hoje - timedelta(days=1)
    def __init__(self,idhabito,idusuario,descricao,status):
        self._idhabito = idhabito
        self._idusuario = idusuario
        self._data = self.hoje.strftime("%Y-%m-%d")
        self._descricao = descricao
        self._status = status
    @staticmethod
    def get_DataFormatada():
        return date.today().strftime("%Y-%m-%d")




