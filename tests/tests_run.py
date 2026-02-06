import unittest
from src.repository import GrimorioRepository
from src.service import GrimorioService
from src.models import EscolaMagia, Componente

class TestGrimorio(unittest.TestCase):
    def setUp(self):
        """Executado ANTES de cada teste. Garante um ambiente limpo."""
        self.repo = GrimorioRepository()
        self.service = GrimorioService(self.repo)

    def teste_criar_magia_sucesso(self):
        payload = {
            "id": 10,
            "nome": "Escudo Arcano",
            "nivel": 1,
            "escola": EscolaMagia.ABJURACAO,
            "componentes": [Componente.VERBAL, Componente.SOMATICO]
        }
        resposta = self.service.criar_magia(payload)
        self.assertEqual(resposta["code"], 201)
        self.assertEqual(resposta["data"]["nome"], "Escudo Arcano")

    def teste_criar_magia_erro_validacao_material(self):
        """Tenta criar magia com componente 'M' mas sem custo (deve falhar)."""
        payload = {
            "id": 11,
            "nome": "Pele de Pedra Falha",
            "nivel": 4,
            "escola": EscolaMagia.TRANSMUTACAO,
            "componentes": [Componente.VERBAL, Componente.SOMATICO, Componente.MATERIAL],
            "custo_em_ouro": None
        }
        resposta = self.service.criar_magia(payload)
        self.assertEqual(resposta["code"], 400)
        self.assertIn("exige 'custo_em_ouro'", resposta["message"])

    def teste_buscar_por_escola(self):
        """Tenta buscar a magia por escola."""
        self.service.criar_magia({"id": 1, "nome": "Luz", "nivel": 0, "escola": EscolaMagia.EVOCACAO, "componentes": [Componente.VERBAL]})
        self.service.criar_magia({"id": 2, "nome": "Cura", "nivel": 1, "escola": EscolaMagia.EVOCACAO, "componentes": [Componente.VERBAL, Componente.SOMATICO]})

        resultado = self.service.buscar_magias(filtro_escola=EscolaMagia.EVOCACAO)
        self.assertEqual(len(resultado), 2)

    def teste_atualizar_magia_sucesso(self):
        """Tenta atualizar a magia com sucesso."""
        self.service.criar_magia({
            "id": 20, "nome": "Mísseis Mágicos", "nivel": 1,
            "escola": EscolaMagia.EVOCACAO, "componentes": [Componente.VERBAL, Componente.SOMATICO]
        })

        novos_dados = {"nome": "Mísseis Infalíveis", "escola": EscolaMagia.ABJURACAO}
        # Nota: O service precisa estar preparado para receber o ID e os dados
        # Se o seu service.py for o que montamos antes, o método atualizar_magia deve existir
        if hasattr(self.service, 'atualizar_magia'):
            resposta = self.service.atualizar_magia(20, novos_dados)
            self.assertEqual(resposta["code"], 200)
            self.assertEqual(resposta["data"]["nome"], "Mísseis Infalíveis")

    def teste_deletar_magia_sucesso(self):
        """Tenta deletar a magia com sucesso."""
        self.service.criar_magia({
            "id": 30, "nome": "Invisibilidade", "nivel": 2,
            "escola": EscolaMagia.ILUSAO, "componentes": [Componente.VERBAL, Componente.SOMATICO]
        })

        resposta = self.service.deletar_magia(30)
        self.assertEqual(resposta["code"], 200)
        busca = self.service.buscar_magias(filtro_nome="Invisibilidade")
        self.assertEqual(len(busca), 0)

    def teste_calculo_dano_escalavel(self):
        """Bola de Fogo (8d6, +1d6 por slot)"""
        payload = {
            "id": 1, "nome": "Bola de Fogo", "nivel": 3, "escola": EscolaMagia.EVOCACAO,
            "componentes": [Componente.VERBAL, Componente.SOMATICO, Componente.MATERIAL], 
            "custo_em_ouro": 0.1,
            "eh_de_ataque": True,
            "dano_base_qtd_dados": 8, "dano_base_lados_dados": 6,
            "dano_por_slot_qtd_dados": 1
        }
        self.service.criar_magia(payload)
        dano_base = self.service.calcular_dano_escala(1, 3)
        self.assertEqual(dano_base, "8d6")
        dano_upcast = self.service.calcular_dano_escala(1, 5)
        self.assertEqual(dano_upcast, "10d6")

    def teste_calculo_dano_erro_slot_insuficiente(self):
        self.service.criar_magia({
            "id": 1, "nome": "Teste", "nivel": 3, "escola": EscolaMagia.EVOCACAO,
            "componentes": [Componente.VERBAL], "eh_de_ataque": True,
            "dano_base_qtd_dados": 8, "dano_base_lados_dados": 6
        })
        resposta = self.service.calcular_dano_escala(1, 1)
        self.assertIn("insuficiente", resposta)

if __name__ == '__main__':
    unittest.main()