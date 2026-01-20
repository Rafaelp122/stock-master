# Decisões de Arquitetura - StockMaster

Este documento serve como índice e resumo das principais decisões arquiteturais do projeto. Para detalhes completos de cada decisão, consulte os arquivos individuais em [`adr/`](adr/).

---

## Architecture Decision Records (ADR)

### ✅ Implementadas

- **[ADR-001: Uso de Docker para Containerização](adr/0001-uso-do-docker.md)** (14/12/2025)
  - Docker e Docker Compose para ambiente padronizado
  
- **[ADR-002: Definição de Stack Tecnológica](adr/0002-stack-tecnologica.md)** (14/12/2025)
  - Django REST Framework + React + PostgreSQL
  
- **[ADR-003: Uso de Makefile para Automação](adr/0003-uso-do-makefile.md)** (14/12/2025)
  - Comandos simplificados para o projeto
  
- **[ADR-004: Estrutura de Apps Django](adr/0004-estrutura-de-apps-django.md)** (14/12/2025)
  - Organização modular por domínio
  
- **[ADR-005: Uso de JWT para Autenticação](adr/0005-jwt-autenticacao.md)** (17/12/2025)
  - Autenticação stateless com SimpleJWT
  
- **[ADR-006: Frontend com React + Vite](adr/0006-frontend-react-vite.md)** (06/01/2026)
  - Build ultrarrápido e HMR instantâneo
  
- **[ADR-007: Tailwind CSS + shadcn/ui](adr/0007-tailwind-shadcn.md)** (06/01/2026)
  - Framework de estilização e componentes acessíveis
  
- **[ADR-008: Autenticação Obrigatória por Padrão](adr/0008-autenticacao-obrigatoria.md)** (07/01/2026)
  - Segurança por padrão em todas as views
  
- **[ADR-009: CORS para Desenvolvimento Local](adr/0009-cors-desenvolvimento.md)** (17/01/2026)
  - Configuração para comunicação frontend/backend
  
- **[ADR-010: Pipeline de Qualidade](adr/0010-pipeline-qualidade.md)** (17/01/2026)
  - Ruff, Pre-commit, Pytest e padronização VS Code
  
- **[ADR-011: Identidade de Produtos via UUIDv7](adr/0011-identidade-produtos-uuidv7.md)** (19/01/2026)
  - SKU sequencial e QR Code dinâmico

- **[ADR-013: Padronização do Registo de Decisões Arquiteturais](adr/0013-padronizacao-registro-adr.md)** (20/01/2026)
  - Ficheiros individuais para ADRs em docs/adr/

### 🏗️ Propostas

- **[ADR-012: Restrição de Acesso aos Arquivos de Mídia](adr/0012-restricao-acesso-media.md)** (20/01/2026)
  - View protegida para servir QR Codes (Issue #15)

---

---

## Visão Geral da Arquitetura

### Stack Tecnológica
- **Backend:** Django REST Framework + PostgreSQL
- **Frontend:** React + Vite + Tailwind CSS + shadcn/ui
- **Infraestrutura:** Docker + Docker Compose
- **Autenticação:** JWT (SimpleJWT)
- **Qualidade:** Ruff + Pre-commit + Pytest

### Estrutura do Projeto
```
stock-master/
├── backend/
│   ├── apps/
│   │   ├── users/      # Gestão de usuários
│   │   └── products/   # Produtos e estoque
│   └── config/         # Configurações Django
├── frontend/
│   └── src/
│       ├── components/ # Componentes React
│       ├── pages/      # Páginas da aplicação
│       └── services/   # Integração com API
├── docs/
│   └── adr/           # Architecture Decision Records
└── docker-compose.yml
```

---

## Próximas Decisões a Documentar

- [ ] Estratégia de implementação da lógica de movimentação de estoque (Issue #6)
- [ ] Política de logs de auditoria para conformidade (Audit Log)
- [ ] Estratégia de deploy (Docker em produção)
- [ ] Política de versionamento de API
- [ ] Estratégia de backup de banco de dados
- [ ] Logging e monitoramento
- [ ] Estratégia de implementação da leitura de QR Code (RF10)

---

## Como Atualizar Este Documento

Ao tomar uma decisão arquitetural importante:

1. Crie uma nova seção ADR-XXX (incrementando o número)
2. Preencha: Data, Status, Contexto, Decisão, Consequências
3. Referencie arquivos/linhas afetadas e requisitos (REQUIREMENTS.MD)
4. Mantenha o histórico (não delete ADRs antigas, marque como "Substituído" se necessário)

---

*Este documento evolui com o projeto. Última atualização: 20/01/2026*
