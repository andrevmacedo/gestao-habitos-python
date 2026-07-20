from models.registros import Registros
from datetime import datetime
class Streak:
    def __init__(self,idusuario,streakatual,melhorstreak):
        self._idusuario = idusuario
        self._streakatual = streakatual
        self._melhorstreak = melhorstreak
    