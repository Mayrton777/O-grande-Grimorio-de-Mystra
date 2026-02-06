from enum import Enum
from pydantic import BaseModel, Field, model_validator
from typing import List, Optional

class EscolaMagia(str, Enum):
    ABJURACAO = "Abjuração"
    CONJURACAO = "Conjuração"
    ADIVINHACAO = "Adivinhação"
    ENCANTAMENTO = "Encantamento"
    EVOCACAO = "Evocação"
    ILUSAO = "Ilusão"
    NECROMANCIA = "Necromancia"
    TRANSMUTACAO = "Transmutação"

class Componente(str, Enum):
    VERBAL = "V"
    SOMATICO = "S"
    MATERIAL = "M"

class Magia(BaseModel):
    id: int
    nome: str
    nivel: int = Field(..., ge=0, le=9)
    escola: EscolaMagia
    componentes: List[Componente]
    custo_em_ouro: Optional[float] = Field(None, ge=0)
    eh_de_ataque: bool = False
    dano_base_qtd_dados: Optional[int] = None
    dano_base_lados_dados: Optional[int] = None
    dano_por_slot_qtd_dados: Optional[int] = None

    @model_validator(mode='after')
    def validar_custo_material(self):
        if Componente.MATERIAL in self.componentes:
            if self.custo_em_ouro is None:
                raise ValueError(f"A magia '{self.nome}' exige 'custo_em_ouro' pois possui componente Material.")
        return self