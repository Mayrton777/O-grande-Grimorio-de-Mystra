from typing import List, Optional
from .models import Magia

class GrimorioRepository:
    def __init__(self):
        self._db: List[Magia] = []

    def salvar(self, magia: Magia) -> Magia:
        if any(m.id == magia.id for m in self._db):
            raise ValueError(f"ID {magia.id} já existe.")
        self._db.append(magia)
        return magia

    def listar_todas(self) -> List[Magia]:
        return self._db

    def buscar_por_id(self, id_magia: int) -> Optional[Magia]:
        return next((m for m in self._db if m.id == id_magia), None)

    def deletar(self, id_magia: int) -> bool:
        original_len = len(self._db)
        self._db = [m for m in self._db if m.id != id_magia]
        return len(self._db) < original_len