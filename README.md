# O Grande Grimório de Mystra 🧙‍♂️

Este projeto é um sistema robusto de gerenciamento de magias (CRUD) baseado nas regras de D&D 5e. Foi desenvolvido como um desafio técnico para demonstrar competências avançadas em **Arquitetura de Software**, **Desenvolvimento Back-End** e **Qualidade de Software (QA)**.

## 🏛️ Arquitetura e Padrões de Projeto

O projeto segue princípios de **Clean Architecture**, garantindo que a aplicação seja fácil de testar e manter:

* **Repository Pattern:** Abstração da camada de dados, permitindo a troca da persistência (ex: de Memória para PostgreSQL) sem afetar a lógica de negócio.
* **Service Layer:** Camada intermediária que encapsula todas as regras de negócio e cálculos matemáticos.
* **Domain Modeling:** Uso de tipagem forte e validações granulares com **Pydantic**, garantindo a integridade dos dados antes mesmo de chegarem ao repositório.
* **SOLID:** Aplicação prática dos princípios de responsabilidade única e inversão de dependência.


## 🚀 Tecnologias Utilizadas

* **Python 3.12**
* **Pydantic v2:** Validação de esquemas e serialização de dados.
* **Unittest:** Framework nativo para garantir a confiabilidade do sistema.

## 📁 Estrutura do Projeto

```text
├── main.py              # Ponto de entrada e demonstração da aplicação
├── src/
│   ├── __init__.py      # Exportação modular dos pacotes
│   ├── models.py        # Esquemas de dados e Enums de domínio
│   ├── repository.py    # Implementação da persistência (Fake DB)
│   └── service.py       # Core da aplicação (CRUD e Regra de Ouro)
├── tests/
│   └── tests_run.py     # Script de automação e descoberta de testes
├── requirements.txt     # Gerenciamento de dependências
└── .gitignore           # Proteção de ambiente virtual e arquivos sensíveis
```

## 🧪 Qualidade e Testes (QA)

A "Regra de Ouro" (cálculo de dano escalável por slot) e todas as operações de CRUD possuem testes automatizados. Para executar a suíte de testes e validar a integridade do sistema, utilize:

```bash
# Execução via módulo para garantir a resolução correta de imports
python3 -m tests.tests_run
```

**Desenvolvido por:** Mayrton Eduardo