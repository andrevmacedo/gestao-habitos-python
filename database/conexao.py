import sqlite3
import warnings
warnings.filterwarnings('ignore', 
    message='The default date adapter is deprecated')

class SQL:
    def __init__(self):
        self.caminhodb = "C:/Users/André Vítor/Desktop/GestaoHabitos/database/banco.db"
        self.conn = sqlite3.connect(self.caminhodb)
        self.cursor = self.conn.cursor()
    def ConfirmarEmail(self,email):
        self.cursor.execute('''
                        select * from usuarios where email = ?
                            ''',(email,))
        return self.cursor.fetchone()
    def CadastrarUsuarioBanco(self,usuario):
        self.cursor.execute('''
                        insert into usuarios values (?,?,?,?,?)
                          ''', (None,usuario._nome,usuario._email,usuario._senha,1))
        self.conn.commit()
        return self.cursor.lastrowid #RETORNA ÚLTIMO ID CRIADO
    def VerificarLogin(self,email,senha):
        self.cursor.execute('''
                        select * from usuarios where email = ? and senha = ? and status = 1
                            ''',(email,senha))
        return self.cursor.fetchone()
    def CriarHabito(self,habito,usuario):
        self.cursor.execute('''
                        insert into habito values (?,?,?,?,?,?)
                            ''', (None,usuario[0],habito._nome,habito._descricao,habito._dificuldade,1))
        self.conn.commit()
        return self.cursor.lastrowid
    def ConsultarIDLogin(self,usuario):
        self.cursor.execute("select id_usuario from usuarios where email = ?",(usuario,))
        return self.cursor.fetchone()
    def ConsultarHabtio(self,id,usuario):
        self.cursor.execute('''
                        select habito.id_habito,habito.id_usuario,usuarios.id_usuario,usuarios.email,habito.nome,habito.descricao,habito.dificuldade,
                            case 
                                when habito.status = 1 then 'Ativo'
                                else 'Desativado'
                            end as status_texto
                        from habito
                        inner join usuarios on habito.id_usuario = usuarios.id_usuario
                        where habito.id_habito = ? and habito.id_usuario = ?
                            ''',(id,usuario[0],))
        return self.cursor.fetchone()
    def AlterarHabito(self,coluna,alterar,id):
        try:
            sql = (f'''
                update habito
                set {coluna} = ?
                where id_habito = ?
                ''')
            self.conn.execute(sql,(alterar,id))
            self.conn.commit()
            return True
        except sqlite3.Error as erro:
            return erro
    def AlterarStatusHabito(self,idhabito):
        self.conn.execute('''
                update habito
                set status =
                    case
                        when status = 1 then 0
                        else 1
                    end
                where id_habito = ?
                          ''',(idhabito,))
        self.conn.commit()
    def ExcluirHabito(self,idhabito):
         self.conn.execute("delete from habito where id_habito = ?",(idhabito,))
         self.conn.commit()
    def ConsultarTodosHabitos(self,idusuario):
        try:
            self.cursor.execute('''
                        select habito.id_habito,habito.id_usuario,usuarios.id_usuario,usuarios.email,habito.nome,habito.descricao,habito.dificuldade,
                            case 
                                when habito.status = 1 then 'Ativo'
                                else 'Desativado'
                            end as status_texto  
                        from habito
                        inner join usuarios on habito.id_usuario = usuarios.id_usuario
                        where habito.id_usuario = ?
                                ''',(idusuario[0],))
            return self.cursor.fetchall()
        except sqlite3.Error as erro:
            return erro
    def CadastrarRegistro(self,registro):
        self.cursor.execute("insert into registro values (?,?,?,?,?,?)",(None,registro._idhabito,registro._idusuario,registro._data,registro._descricao,registro._status))
        self.conn.commit()
        return self.cursor.lastrowid
    def VerificarRegistroDiario(self,idhabito,data):
        self.cursor.execute('''
                        select * from registro where id_habito = ? and data = ?
                            ''',(idhabito,data,))
        return self.cursor.fetchone()
    def ConsultarHabitosNaoConcluidos(self,usuario,data):
        self.cursor.execute('''
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
        return self.cursor.fetchall()
    def RegistrarHabitosNAOFeitos(self,idhabito,idusuario,ontem):
        self.conn.execute('''
                insert into registro values (?,?,?,?,?,?)
                          ''',(None,idhabito,idusuario,ontem,"Não Realizado",0))
        self.conn.commit()
    def ConsultarRegistroNAOFeito(self,idhabito,data):
        self.cursor.execute('''
                select registro.id_registro, registro.id_habito, registro.data, registro.status, habito.nome, habito.descricao, habito.dificuldade,
                    case registro.status
                        when 1 then 'Realizado'
                        else 'Não Realizado'
                    end as status_texto
                from registro 
                inner join habito on habito.id_habito = registro.id_habito
                where registro.id_habito = ? and registro.data = ? and registro.status = 0
                            ''',(idhabito,data,))
        return self.cursor.fetchone()
    def AlterarRegistro(self,usuario,idhabito,descricao,data):
        try:
            self.cursor.execute('''
                    update registro
                    set nota = ?, status = 1
                    where id_usuario = ? and id_habito = ? and data = ?
                            ''',(descricao,usuario[0],idhabito,data))
            self.conn.commit()
            return True
        except sqlite3.Error as erro:
            return erro
    def TotalHabitos(self,usuario):
        self.cursor.execute('''
                select count(habito.id_usuario)
                from habito
                where habito.id_usuario = ? 
                group by habito.id_usuario
                            ''',(usuario[0],))
        return self.cursor.fetchone()
    def HabitosConclAband(self,usuario):
        self.cursor.execute('''
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
        return self.cursor.fetchone()
    def MelhorHabito(self,usuario):
        self.cursor.execute('''
                select count(registro.id_habito) as total,habito.nome
                from registro
                inner join habito on habito.id_habito = registro.id_habito
                where registro.id_usuario = ?
                and registro.status = 1
                group by registro.id_habito,habito.nome
                order by total desc
                limit 1
                            ''',(usuario[0],))
        return self.cursor.fetchone()
    def ListarHabitosConcluidosHoje(self,usuario,data):
        self.cursor.execute('''
                select registro.id_habito, habito.nome, habito.descricao, habito.dificuldade, registro.data, registro.nota, registro.status,
                    case
                        when registro.status = 1 then 'Realizado'
                        else 'Não Realizado'
                    end
                from registro
                inner join habito on registro.id_habito = habito.id_habito
                where registro.id_usuario = ? and registro.data = ? and registro.status = 1
                            ''',(usuario[0],data,))
        return self.cursor.fetchall()
    def ListarHabitosNConcluidosHoje(self,usuario,data):
        self.cursor.execute('''
                select h.id_habito, h.nome, h.dificuldade, h.descricao
                from habito h
                where h.id_usuario = ? and h.status = 1
                and not exists (
                    select 1
                    from registro r
                    where r.id_habito = h.id_habito
                    and r.data = ?
                            )''',(usuario[0],data,))
        return self.cursor.fetchall()
    def SteakAtual(self,usuario):
        self.cursor.execute('''
                select distinct(r.data)
                from registro r
                where r.id_usuario = ?
                and r.status = 1
                order by r.data desc
                            ''',(usuario[0],))
        return self.cursor.fetchall()
    def SteakPorHabito(self,usuario):
        self.cursor.execute('''
                select distinct group_concat(r.data),h.nome
                from registro r
                inner join habito h on h.id_habito = r.id_habito
                where r.id_usuario = ?
                and r.status = 1
                and h.status = 1
                group by h.id_habito
                order by r.data,h.id_habito desc
                            ''',(usuario[0],))
        return self.cursor.fetchall()
    def BuscarIDHabitosSequencia(self,dados):
        query = f"select id_habito from habito where nome in ({','.join(['?']*len(dados))})"
        self.cursor.execute(query,dados)
        return self.cursor.fetchall()
    def RegistrarStreakHabitos(self,registros):
        self.conn.executemany(''' insert or ignore into steak values (?,?,?,?,?)
                          ''',registros)
        self.conn.commit()
    def RegistrarStreakUnico(self,registro):
        self.conn.execute(''' insert or ignore into streak_geral values (?,?,?)
                          ''',(registro._idusuario,registro._streakatual,registro._melhorstreak))
        self.conn.commit()
    def AtualizarStreakUnico(self,registro):
        self.conn.execute('''
                update streak_geral
                set streak = ?,
                    melhor_streak = MAX(melhor_streak,?)
                where id_usuario = ?             
                             ''',(registro._streakatual,registro._melhorstreak,registro._idusuario))
        return self.conn.commit()
    def BuscarMelhorStreak(self,usuario):
        self.cursor.execute('''
                select melhor_streak from streak_geral where id_usuario = ?
                            ''',(usuario[0],))
        return self.cursor.fetchone()
    def AtualizarStreakHabitos(self,registros):
        self.conn.executemany('''
                update steak
                set steak_atual = ?,
                    melhor_steak = MAX(melhor_steak, ?)
                where id_usuario = ? and id_habito = ?
                              ''', registros)
        self.conn.commit()
    def RankingGeral(self):
        self.cursor.execute('''
                select u.email,s.streak
                from usuarios u
                inner join streak_geral s on u.id_usuario = s.id_usuario
                order by s.streak desc
                            ''')
        return self.cursor.fetchall()
    def TaxaDeConclusao(self):
        self.cursor.execute('''
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
        return self.cursor.fetchall()
    def HabitosMaisConsistentes(self):
        self.cursor.execute('''
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
        return self.cursor.fetchall()
    def DiasMaisProdutivos(self):
        self.cursor.execute('''
                select r.data, count(r.data) as rep
                from registro r
                where r.status = 1
                group by r.data
                order by rep desc
                limit 2
                            ''')
        return self.cursor.fetchall()
    def UsuariosBaixoDesempenho(self):
        self.cursor.execute('''
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
        return self.cursor.fetchall()


db = SQL() #objeto de serviço (DAO), sem estado global
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