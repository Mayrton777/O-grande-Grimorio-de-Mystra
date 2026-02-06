from typing import List
from .repository import GrimorioRepository
from .models import Magia

class GrimorioService:
    def __init__(self, repository: GrimorioRepository):
        self.repo = repository

    def criar_magia(self, dados_brutos: dict) -> dict:
        try:
            nova_magia = Magia(**dados_brutos)
            self.repo.salvar(nova_magia)
            return {"status": "success", "data": nova_magia.model_dump(), "code": 201}
        except Exception as e:
            return {"status": "error", "message": str(e), "code": 400}

    def buscar_magias(self, filtro_nome: str = None, filtro_escola: str = None) -> List[dict]:
        resultado = self.repo.listar_todas()
        if filtro_nome:
            resultado = [m for m in resultado if filtro_nome.lower() in m.nome.lower()]
        if filtro_escola:
            resultado = [m for m in resultado if m.escola == filtro_escola]
        return [m.model_dump() for m in resultado]

    def deletar_magia(self, id_magia: int) -> dict:
        sucesso = self.repo.deletar(id_magia)
        if sucesso:
            return {"status": "success", "message": "Removida.", "code": 200}
        return {"status": "error", "message": "Não encontrada.", "code": 404}

    def atualizar_magia(self, id_magia: int, dados_atualizados: dict) -> dict:
        magia_existente = self.repo.buscar_por_id(id_magia)
        if not magia_existente:
            return {"status": "error", "message": "Não encontrada.", "code": 404}
        
        dados_finais = magia_existente.model_dump()
        dados_finais.update(dados_atualizados)
        dados_finais['id'] = id_magia
        
        try:
            magia_validada = Magia(**dados_finais)
            self.repo.deletar(id_magia)
            self.repo.salvar(magia_validada)
            return {"status": "success", "data": magia_validada.model_dump(), "code": 200}
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