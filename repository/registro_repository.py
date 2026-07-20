class RegistroRepository:
    def __init__(self,db):
        self._db = db
    def CadastrarRegistro(self,registro):
        self._db.cursor.execute("insert into registro values (?,?,?,?,?,?)",(None,registro._idhabito,registro._idusuario,registro._data,registro._descricao,registro._status))
        self._db.commit()
        return self._db.cursor.lastrowid
    def VerificarRegistroDiario(self,idhabito,data):
        self._db.cursor.execute('''
                        select * from registro where id_habito = ? and data = ?
                            ''',(idhabito,data,))
        return self._db.cursor.fetchone()
    def ConsultarHabitosNaoConcluidos(self,usuario,data):
        self._db.cursor.execute('''
                select habito.id_usuario, habito.id_habito
                from habito
                where habito.id_usuario = ?
                and habito.status = 1
                and not exists (
                    select 1 
                    from registro
                    where registro.id_habito = habito.id_habito
                    and registro.data = ?)
                            ''',(usuario[0],data,))
        return self._db.cursor.fetchall()
    def RegistrarHabitosNAOFeitos(self,registros):
        self._db.conn.executemany('''
                insert into registro values (?,?,?,?,?,?)
                          ''',registros)
        self._db.commit()
    def ConsultarRegistroNAOFeito(self,idhabito,data):
        self._db.cursor.execute('''
                select registro.id_registro, registro.id_habito, registro.data, registro.status, habito.nome, habito.descricao, habito.dificuldade,
                    case registro.status
                        when 1 then 'Realizado'
                        else 'Não Realizado'
                    end as status_texto
                from registro 
                inner join habito on habito.id_habito = registro.id_habito
                where registro.id_habito = ? and registro.data = ? and registro.status = 0
                            ''',(idhabito,data,))
        return self._db.cursor.fetchone()
    def AlterarRegistro(self,usuario,idhabito,descricao,data):
        try:
            self._db.cursor.execute('''
                    update registro
                    set nota = ?, status = 1
                    where id_usuario = ? and id_habito = ? and data = ?
                            ''',(descricao,usuario[0],idhabito,data))
            self._db.commit()
            return True
        except Exception as erro:
            return erro
    def ListarHabitosConcluidosHoje(self,usuario,data):
        self._db.cursor.execute('''
                select registro.id_habito, habito.nome, habito.descricao, habito.dificuldade, registro.data, registro.nota, registro.status,
                    case
                        when registro.status = 1 then 'Realizado'
                        else 'Não Realizado'
                    end
                from registro
                inner join habito on registro.id_habito = habito.id_habito
                where registro.id_usuario = ? and registro.data = ? and registro.status = 1
                            ''',(usuario[0],data,))
        return self._db.cursor.fetchall()
    def ListarHabitosNConcluidosHoje(self,usuario,data):
        self._db.cursor.execute('''
                select h.id_habito, h.nome, h.dificuldade, h.descricao
                from habito h
                where h.id_usuario = ? and h.status = 1
                and not exists (
                    select 1
                    from registro r
                    where r.id_habito = h.id_habito
                    and r.data = ?
                            )''',(usuario[0],data,))
        return self._db.cursor.fetchall()
    def StreakAtual(self,usuario):
        self._db.cursor.execute('''
                select distinct(r.data)
                from registro r
                where r.id_usuario = ?
                and r.status = 1
                order by r.data desc
                            ''',(usuario[0],))
        return self._db.cursor.fetchall()
    def StreakPorHabito(self,usuario):
        self._db.cursor.execute('''
                select distinct group_concat(r.data),h.nome
                from registro r
                inner join habito h on h.id_habito = r.id_habito
                where r.id_usuario = ?
                and r.status = 1
                and h.status = 1
                group by h.id_habito
                order by r.data,h.id_habito desc
                            ''',(usuario[0],))
        return self._db.cursor.fetchall()
    def TaxaDeConclusao(self):
        self._db.cursor.execute('''
                select count(r.status), u.email,
                    sum(case
                        when r.status = 1 then 1
                        else 0
                    end) as realizado,
                    (sum(r.status = 1) * 100.0 / COUNT(*)) AS taxa
                from registro r
                inner join usuarios u on u.id_usuario = r.id_usuario
                group by r.id_usuario
                order by taxa desc
                            ''')
        return self._db.cursor.fetchall()
    def HabitosMaisConsistentes(self):
        self._db.cursor.execute('''
                SELECT 
                    r.id_usuario,
                    u.email,
                    h.nome,
                    COUNT(*) as total
                FROM registro r
                INNER JOIN habito h ON h.id_habito = r.id_habito
                INNER JOIN usuarios u ON u.id_usuario = r.id_usuario
                WHERE r.status = 1
                GROUP BY r.id_usuario, r.id_habito
                HAVING COUNT(*) = (
                    SELECT MAX(cont)
                    FROM (
                        SELECT COUNT(*) as cont
                        FROM registro r2
                        WHERE r2.id_usuario = r.id_usuario
                        AND r2.status = 1
                        GROUP BY r2.id_habito
                    )
                )
                ORDER BY total DESC
                            ''')
        return self._db.cursor.fetchall()
    def DiasMaisProdutivos(self):
        self._db.cursor.execute('''
                select r.data, count(r.data) as rep
                from registro r
                where r.status = 1
                group by r.data
                order by rep desc
                limit 2
                            ''')
        return self._db.cursor.fetchall()
    def UsuariosBaixoDesempenho(self):
        self._db.cursor.execute('''
                select count(r.status), u.email,
                    sum(case
                        when r.status = 1 then 1
                        else 0
                    end) as realizado,
                    (sum(r.status = 1) * 100.0 / COUNT(*)) AS taxa
                from registro r
                inner join usuarios u on u.id_usuario = r.id_usuario
                group by r.id_usuario
                having (sum(r.status = 1) * 100.0 / COUNT(*)) < 60
                order by taxa asc
                            ''')
        return self._db.cursor.fetchall()
    def HabitosConclAband(self,usuario):
        self._db.cursor.execute('''
                select count(registro.status),
                    sum(case 
                            when registro.status = 1 then 1
                        else 0
                    end),
                    sum(case 
                            when registro.status = 0 then 1
                        else 0
                    end)  
                from registro
                where registro.id_usuario = ?
                            ''',(usuario[0],))
        return self._db.cursor.fetchone()