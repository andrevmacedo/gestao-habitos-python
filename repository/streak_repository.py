class StreakRepository:
    def __init__(self,db):
        self._db = db
    def RegistrarStreakHabitos(self,registros):
        self._db.conn.executemany(''' insert or ignore into steak values (?,?,?,?,?)
                          ''',registros)
        self._db.commit()
    def RegistrarStreakUnico(self,registro):
        self._db.conn.execute(''' insert or ignore into streak_geral values (?,?,?)
                          ''',(registro._idusuario,registro._streakatual,registro._melhorstreak))
        self._db.commit()
    def AtualizarStreakUnico(self,registro):
        self._db.conn.execute('''
                update streak_geral
                set streak = ?,
                    melhor_streak = MAX(melhor_streak,?)
                where id_usuario = ?             
                             ''',(registro._streakatual,registro._melhorstreak,registro._idusuario))
        return self._db.commit()
    def BuscarMelhorStreak(self,usuario):
        self._db.cursor.execute('''
                select melhor_streak from streak_geral where id_usuario = ?
                            ''',(usuario[0],))
        return self._db.cursor.fetchone()
    def AtualizarStreakHabitos(self,registros):
        self._db.conn.executemany('''
                update steak
                set steak_atual = ?,
                    melhor_steak = MAX(melhor_steak, ?)
                where id_usuario = ? and id_habito = ?
                              ''', registros)
        self._db.commit()
    def RankingGeral(self):
        self._db.cursor.execute('''
                select u.email,s.streak
                from usuarios u
                inner join streak_geral s on u.id_usuario = s.id_usuario
                order by s.streak desc
                            ''')
        return self._db.cursor.fetchall()