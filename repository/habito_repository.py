class HabitoRepository:
    def __init__(self,db):
        self._db = db
    def CriarHabito(self,habito,usuario):
        self._db.cursor.execute('''
                        insert into habito values (?,?,?,?,?,?)
                            ''', (None,usuario[0],habito._nome,habito._descricao,habito._dificuldade,1))
        self._db.commit()
        return self._db.cursor.lastrowid
    def ConsultarHabito(self,id,usuario):
        self._db.cursor.execute('''
                        select habito.id_habito,habito.id_usuario,usuarios.id_usuario,usuarios.email,habito.nome,habito.descricao,habito.dificuldade,
                            case 
                                when habito.status = 1 then 'Ativo'
                                else 'Desativado'
                            end as status_texto
                        from habito
                        inner join usuarios on habito.id_usuario = usuarios.id_usuario
                        where habito.id_habito = ? and habito.id_usuario = ?
                            ''',(id,usuario[0],))
        return self._db.cursor.fetchone()
    def AlterarHabito(self,coluna,alterar,id):
        try:
            sql = (f'''
                update habito
                set {coluna} = ?
                where id_habito = ?
                ''')
            self._db.conn.execute(sql,(alterar,id))
            self._db.commit()
            return True
        except Exception as erro:
            return erro
    def AlterarStatusHabito(self,idhabito):
        self._db.conn.execute('''
                update habito
                set status =
                    case
                        when status = 1 then 0
                        else 1
                    end
                where id_habito = ?
                          ''',(idhabito,))
        self._db.commit()
    def ExcluirHabito(self,idhabito):
         self._db.conn.execute("delete from habito where id_habito = ?",(idhabito,))
         self._db.commit()
    def ConsultarTodosHabitos(self,idusuario):
        self._db.cursor.execute('''
                    select habito.id_habito,habito.id_usuario,usuarios.id_usuario,usuarios.email,habito.nome,habito.descricao,habito.dificuldade,
                        case 
                            when habito.status = 1 then 'Ativo'
                            else 'Desativado'
                        end as status_texto  
                    from habito
                    inner join usuarios on habito.id_usuario = usuarios.id_usuario
                    where habito.id_usuario = ?
                            ''',(idusuario[0],))
        return self._db.cursor.fetchall()
    def BuscarIDHabitosSequencia(self,dados):
        try:
            query = f"select id_habito from habito where nome in ({','.join(['?']*len(dados))})"
            self._db.cursor.execute(query,dados)
            return self._db.cursor.fetchall()
        except Exception as erro:
            return erro
    def MelhorHabito(self,usuario):
        self._db.cursor.execute('''
                select count(registro.id_habito) as total,habito.nome
                from registro
                inner join habito on habito.id_habito = registro.id_habito
                where registro.id_usuario = ?
                and registro.status = 1
                group by registro.id_habito,habito.nome
                order by total desc
                limit 1
                            ''',(usuario[0],))
        return self._db.cursor.fetchone()
    def TotalHabitos(self,usuario):
        self._db.cursor.execute('''
                select count(habito.id_usuario)
                from habito
                where habito.id_usuario = ? 
                group by habito.id_usuario
                            ''',(usuario[0],))
        return self._db.cursor.fetchone()