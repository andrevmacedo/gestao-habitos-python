from models.habitos import Habitos
from repository.habito_repository import HabitoRepository
from database.conexao import db
repo = HabitoRepository(db)