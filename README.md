# O Grande Grimório de Mystra 🧙‍♂️

Este projeto é um sistema de gerenciamento de magias (CRUD) inspirado nas regras de D&D 5e, desenvolvido como um desafio técnico para demonstrar habilidades em Back-End e Arquitetura de Software.

## 🏛️ Arquitetura e Padrões de Projeto

O projeto foi estruturado utilizando boas práticas de desenvolvimento (Clean Code) e os seguintes padrões:

* **Repository Pattern:** Isolamento da camada de persistência de dados.
* **Service Layer:** Camada de lógica de negócio centralizada e desacoplada.
* **Domain Modeling:** Uso de tipagem forte e validações automáticas com **Pydantic**.
* **SOLID:** Foco em responsabilidade única e extensibilidade.

## 🚀 Tecnologias Utilizadas

* **Python 3.12**
* **Pydantic** (Validação de dados e Schemas)
* **Unittest** (Suíte de testes unitários)

## 📁 Estrutura do Projeto

```text
├── main.py              # Ponto de entrada da aplicação
├── src/
│   ├── models.py        # Modelagem de domínio e Enums
│   ├── repository.py    # Persistência em memória (Fake DB)
│   └── service.py       # Regras de negócio e lógica de cálculo
├── tests/               # Testes unitários e de integração
└── .gitignore           # Configurações de arquivos ignorados pelo Git
```

**Desenvolvido por:** Mayrton Eduardo