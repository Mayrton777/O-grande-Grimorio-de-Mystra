from typing import List
from .models import Magia
from .repository import GrimorioRepository

class GrimorioService:
    def __init__(self, repository: GrimorioRepository):
        self.repo = repository

    def criar_magia(self, dados: dict):
        try:
            nova_magia = Magia(**dados)
            self.repo.salvar(nova_magia)
            return {"status": "success", "data": nova_magia.model_dump(), "code": 201}
        except Exception as e:
            return {"status": "error", "message": str(e), "code": 400}

    def calcular_dano_escala(self, id_magia: int, nivel_slot: int) -> str:
        magia = self.repo.buscar_por_id(id_magia)
        if not magia or not magia.eh_de_ataque:
            return "Erro: Magia não encontrada ou não causa dano."
        
        if nivel_slot < magia.nivel:
            return "Erro: Slot insuficiente."

        total_dados = magia.dano_base_qtd_dados + ((nivel_slot - magia.nivel) * (magia.dano_por_slot_qtd_dados or 0))
        return f"{total_dados}d{magia.dano_base_lados_dados}"