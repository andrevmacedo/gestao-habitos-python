# Planejamento de Refatoração — GestaoHabitos

> Siga as fases em ordem. Cada uma depende da anterior.

---

## Progresso geral

| Fase | Descrição | Status |
|------|-----------|--------|
| 1 | Base: corrigir o caminho do banco e a conexão | ⬜ |
| 2 | Models: limpar as entidades (só dados) | ⬜ |
| 3 | Repository: dividir os 50+ métodos da classe SQL | ⬜ |
| 4 | Services: extrair regras de negócio | ⬜ |
| 5 | Views: separar os menus e inputs por entidade | ⬜ |

---

## Fase 1 — Base: corrigir o caminho do banco e a conexão

> **Começar aqui.** Tudo depende da conexão. Sem isso correto, nenhuma outra camada funciona. É o menor risco e maior impacto imediato.

- [ ] Remover o caminho absoluto hardcoded (`C:/Users/André Vítor/...`) — `conexao.py`
- [ ] Usar `os.path.dirname(__file__)` para montar o caminho relativo ao arquivo — `conexao.py`
- [ ] Extrair a classe `SQL` para uma classe `Database` enxuta (só conexão, cursor, commit, close) — `conexao.py`
- [ ] Verificar que o app continua funcionando com a nova conexão antes de avançar — `teste`

### Referência rápida

```python
# database/conexao.py — resultado esperado
import sqlite3
import os

class Database:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._conn = sqlite3.connect(os.path.join(base_dir, "banco.db"))
        self._cursor = self._conn.cursor()

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

db = Database()
```

---

## Fase 2 — Models: limpar as entidades (só dados)

> **Pouco risco.** Mover as funções de menu e input para fora das classes é seguro — você não vai quebrar queries nem lógica de negócio.

- [ ] Manter só `__init__` e `@staticmethod` de validação em `models/usuario.py` — `usuario.py`
- [ ] Manter só `__init__` e `DefinirDificuldade` em `models/habito.py` — `habito.py`
- [ ] Manter só `__init__` e `get_DataFormatada` em `models/registro.py` — `registro.py`
- [ ] Criar `models/streak.py` com só a classe `Streak` (tirar de `consultas_user.py`) — `streak.py`
- [ ] Converter `VerificarEmail` e `ConfirmarSenha` de `@classmethod` para `@staticmethod` — `refactor`

### Estrutura esperada dos models

```
models/
  usuario.py   → class Usuario  (só __init__ + @staticmethod de validação)
  habito.py    → class Habito   (só __init__ + DefinirDificuldade)
  registro.py  → class Registro (só __init__ + get_DataFormatada)
  streak.py    → class Streak   (só __init__ + CalcularStreakGeral + SequenciaPorHabito)
```

---

## Fase 3 — Repository: dividir os 50+ métodos da classe SQL

> **Maior esforço.** Cada repositório recebe a instância do `Database` por injeção. Mova os métodos do `SQL` por entidade — usuário, hábito, registro, streak.

- [ ] Criar `repository/usuario_repository.py` com `ConfirmarEmail`, `CadastrarUsuario`, `VerificarLogin`, `ConsultarIDLogin` — `usuario`
- [ ] Criar `repository/habito_repository.py` com `CriarHabito`, `ConsultarHabito`, `AlterarHabito`, `ExcluirHabito`, `ListarHabitos` — `habito`
- [ ] Criar `repository/registro_repository.py` com `CadastrarRegistro`, `VerificarRegistroDiario`, `AlterarRegistro`, etc. — `registro`
- [ ] Criar `repository/streak_repository.py` com métodos de streak (incluindo renomear typos) — `streak`
- [ ] Corrigir typos: `SteakAtual` → `StreakAtual`, `ConsultarHabtio` → `ConsultarHabito` em todos os lugares — `typos`
- [ ] Atualizar o `main.py` e os models para importar dos novos repositórios — `imports`

### Estrutura esperada dos repositórios

```
repository/
  usuario_repository.py   → queries de usuário
  habito_repository.py    → queries de hábito
  registro_repository.py  → queries de registro
  streak_repository.py    → queries de streak
```

### Padrão de injeção de dependência

```python
# repository/habito_repository.py
class HabitoRepository:
    def __init__(self, db):
        self._db = db

    def criar(self, habito, usuario):
        self._db.cursor.execute(
            "insert into habito values (?,?,?,?,?,?)",
            (None, usuario[0], habito._nome, habito._descricao, habito._dificuldade, 1)
        )
        self._db.commit()
        return self._db.cursor.lastrowid
```

---

## Fase 4 — Services: extrair regras de negócio

> **Organização.** Services orquestram os repositórios. `StreakService` é o mais complexo — `CalcularStreakGeral` e `SequenciaPorHabito` já são lógica de negócio pura.

- [ ] Criar `services/usuario_service.py` com login, logout, cadastro e verificações — `usuario`
- [ ] Criar `services/habito_service.py` com criação, edição e validação de hábitos — `habito`
- [ ] Criar `services/streak_service.py` com `CalcularStreakGeral` e `SequenciaPorHabito` — `streak`
- [ ] Criar `services/admin_service.py` com ranking, taxa, consistência e baixo desempenho — `admin`
- [ ] Mover `AtualizarStreakUsuario` e `HabitosNaoConcluidos` do `main.py` para os services — `main.py`

### Estrutura esperada dos services

```
services/
  usuario_service.py  → login, logout, cadastro
  habito_service.py   → criação, edição, validação
  streak_service.py   → cálculo de streak geral e por hábito
  admin_service.py    → rankings e métricas administrativas
```

---

## Fase 5 — Views: separar os menus e inputs por entidade

> **Finalização.** Esta fase é a mais mecânica — você apenas move funções que já existem. O trabalho duro foi feito nas fases anteriores.

- [ ] Criar `views/usuario_view.py` com `MenuUsuario`, `CadastroUsuario`, `LoginUsuario` — `usuario`
- [ ] Criar `views/habito_view.py` com `MenuHabitos`, `CadastrarHabito`, `EditarHabito`, `MostrarHabito` — `habito`
- [ ] Criar `views/registro_view.py` com `MenuRegistros`, `RegistrarExecucao`, `AtualizarRegistro` — `registro`
- [ ] Criar `views/consultas_view.py` com `MenuConsultas`, `SteakGeral`, `ListarHabitosConcluidos` — `consultas`
- [ ] Criar `views/admin_view.py` com `MenuAdmin` e todos os `Mostrar*` do `consultas_admin.py` — `admin`
- [ ] Limpar `main.py` para só importar views e chamar a view correta por menu — `main.py`

### Estrutura esperada das views

```
views/
  usuario_view.py   → menus e inputs de usuário
  habito_view.py    → menus e inputs de hábito
  registro_view.py  → menus e inputs de registro
  consultas_view.py → menus e exibição de métricas
  admin_view.py     → menus e exibição administrativa
```

### main.py esperado ao final

```python
# main.py — só navegação
from views import usuario_view, habito_view, registro_view, consultas_view, admin_view
from database.conexao import db

def menu():
    while True:
        usuario_logado = ...  # busca do service
        if usuario_logado == "admin@":
            admin_view.menu(db)
        elif usuario_logado:
            menu_logado(usuario_logado)
        else:
            if not usuario_view.menu(db):
                break

if __name__ == "__main__":
    menu()
```

---

## Estrutura final esperada do projeto

```
GestaoHabitos/
  main.py
  database/
    conexao.py          ← só conexão e cursor
    banco.db
  models/
    usuario.py          ← só classe Usuario
    habito.py           ← só classe Habito
    registro.py         ← só classe Registro
    streak.py           ← só classe Streak  (novo)
  repository/           ← antes vazia, agora com 4 arquivos
    usuario_repository.py
    habito_repository.py
    registro_repository.py
    streak_repository.py
  services/             ← antes vazia, agora com 4 arquivos
    usuario_service.py
    habito_service.py
    streak_service.py
    admin_service.py
  views/                ← novo — extraído dos models/
    usuario_view.py
    habito_view.py
    registro_view.py
    consultas_view.py
    admin_view.py
```
