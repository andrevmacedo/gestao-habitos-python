import sqlite3
import warnings
warnings.filterwarnings('ignore', 
    message='The default date adapter is deprecated')
import os

class Database:
    def __init__(self):
        self._caminhodb = os.path.dirname(os.path.abspath(__file__))
        self._conn = sqlite3.connect(os.path.join(self._caminhodb, "banco.db"))
        self._cursor = self.conn.cursor()
    @property
    def conn(self):
        return self._conn
    @property
    def cursor(self):
        return self._cursor
    def commit(self):
        self._conn.commit()
    def close(self):
        self._conn.close()    



db = Database() #objeto de serviço (DAO), sem estado global
#NOVAS FERRAMENTAS UTILIZADAS:
# - CASE
# - GROUP_CONCAT
# - SUM
# - NOT EXISTS
# - EXECUTEMANY
# - .ZIP (Lógica)
# - IN
# - INSERT OR IGNORE
# - MAX
# - ENUMERATE