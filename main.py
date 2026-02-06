from src.repository import GrimorioRepository
from src.service import GrimorioService
from src.models import EscolaMagia, Componente, Magia

def main():
    repo = GrimorioRepository()
    service = GrimorioService(repo)

    # Seed Data
    print("--- Inicializando o Grande Grimório ---")
    service.criar_magia({
        "id": 1, "nome": "Bola de Fogo", "nivel": 3, 
        "escola": EscolaMagia.EVOCACAO, 
        "componentes": [Componente.VERBAL, Componente.SOMATICO, Componente.MATERIAL],
        "custo_em_ouro": 0.1, "eh_de_ataque": True,
        "dano_base_qtd_dados": 8, "dano_base_lados_dados": 6, "dano_por_slot_qtd_dados": 1
    })

    # Testando a Regra de Ouro
    dano = service.calcular_dano_escala(1, 5)
    print(f"Dano da Bola de Fogo em Slot nível 5: {dano}")

if __name__ == "__main__":
    main()