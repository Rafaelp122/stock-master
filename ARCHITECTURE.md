# Decisões de Arquitetura - StockMaster

Este documento registra as principais decisões arquiteturais do projeto StockMaster, incluindo justificativas e implicações.

---

## ADR-001: Uso de Docker para Containerização

**Data:** 14/12/2025  
**Status:** ✅ Implementado  
**Decisão:** Utilizar Docker e Docker Compose para containerização do ambiente de desenvolvimento e produção.

### Contexto
Necessidade de garantir consistência entre ambientes de desenvolvimento, homologação e produção, além de facilitar onboarding de novos desenvolvedores.

### Decisão
- **Docker:** Containerização de aplicações (backend, frontend, banco de dados)
- **Docker Compose:** Orquestração local dos serviços

### Justificativa
- ✅ **Consistência:** "Funciona na minha máquina" = funciona em produção
- ✅ **Isolamento:** Dependências isoladas por container
- ✅ **Onboarding rápido:** `docker-compose up` e ambiente pronto
- ✅ **PostgreSQL:** Facilita uso de banco de dados em desenvolvimento
- ✅ **Deploy simplificado:** Mesma estrutura para produção

### Consequências

**Positivas:**
- ✅ Ambiente padronizado para toda a equipe
- ✅ Fácil reset do ambiente (volumes Docker)
- ✅ Preparação para deploy em cloud (AWS ECS, Google Cloud Run, etc.)

**Negativas:**
- ⚠️ Curva de aprendizado para desenvolvedores sem experiência com Docker
- ⚠️ Overhead de recursos (memória/CPU) vs ambiente nativo

### Implementação
- Arquivo: `docker-compose.yml` (raiz do projeto)
- Containers: backend (Django), frontend (React/Vite), db (PostgreSQL)

---

## ADR-002: Definição de Stack Tecnológica

**Data:** 14/12/2025  
**Status:** ✅ Implementado  
**Decisão:** Stack baseada em Django REST Framework + React + PostgreSQL.

### Contexto
Necessidade de escolher tecnologias maduras, escaláveis e com boa comunidade para um sistema de gestão de estoque.

### Decisão
- **Backend:** Django REST Framework (Python)
- **Frontend:** React com Vite
- **Banco de Dados:** PostgreSQL
- **Autenticação:** JWT (SimpleJWT)

### Justificativa

**Backend - Django REST Framework:**
- ✅ Framework maduro e bem documentado
- ✅ ORM poderoso (abstração de banco de dados)
- ✅ Admin panel nativo
- ✅ Ecossistema rico (bibliotecas para QR Code, exportação, etc.)
- ✅ Segurança built-in (CSRF, SQL injection, XSS)

**Frontend - React:**
- ✅ Biblioteca mais popular para SPAs
- ✅ Componentização reutilizável
- ✅ Vite para build ultrarrápido
- ✅ Ecossistema maduro (routing, state management, etc.)

**Banco de Dados - PostgreSQL:**
- ✅ Robusto para produção
- ✅ Suporte a JSON (flexibilidade futura)
- ✅ Integridade referencial
- ✅ Open-source

### Consequências
- ✅ Stack moderna e escalável
- ✅ Separação clara frontend/backend (arquitetura desacoplada)
- ✅ Facilita contratação (tecnologias populares)

### Referência
- Documento: `REQUIREMENTS.MD` (Stack Tecnológica - RNF)

---

## ADR-003: Uso de Makefile para Automação de Tarefas

**Data:** 14/12/2025  
**Status:** ✅ Implementado  
**Decisão:** Utilizar Makefile para padronizar e simplificar comandos do projeto.

### Contexto
Comandos Docker e Django podem ser longos e difíceis de memorizar. Necessidade de padronizar tarefas comuns entre desenvolvedores.

### Decisão
Criar `Makefile` na raiz do projeto com comandos simplificados.

### Justificativa
- ✅ **Simplicidade:** `make up` ao invés de `docker-compose up -d`
- ✅ **Documentação viva:** Makefile serve como referência de comandos disponíveis
- ✅ **Onboarding:** Novos desenvolvedores aprendem comandos rapidamente
- ✅ **Consistência:** Todos executam comandos da mesma forma
- ✅ **Produtividade:** Reduz tempo digitando comandos complexos

### Comandos Principais
```makefile
make up          # Sobe os containers
make down        # Derruba os containers
make logs        # Mostra logs
make migrate     # Executa migrações
make shell       # Acessa shell do Django
make test        # Executa testes
make format      # Formata código (black, isort)
```

### Consequências

**Positivas:**
- ✅ Reduz erros de digitação em comandos
- ✅ Facilita automação de CI/CD (make test, make deploy)
- ✅ Documentação centralizada de tarefas

**Negativas:**
- ⚠️ Desenvolvedores precisam ter `make` instalado (padrão em Linux/Mac, precisa instalar no Windows)
- ⚠️ Mais uma ferramenta para aprender (curva pequena)

### Implementação
- Arquivo: `Makefile` (raiz do projeto)
- Compatibilidade: Linux, macOS, Windows (via Git Bash ou WSL)

---

## ADR-004: Estrutura de Apps Django

**Data:** 14/12/2025  
**Status:** ✅ Implementado  
**Decisão:** Organizar código em apps Django separados por domínio.

### Contexto
Necessidade de estruturar o backend de forma modular e escalável.

### Estrutura
```
backend/apps/
├── users/      # Gestão de usuários e autenticação
└── products/   # Produtos, categorias e estoque
```

### Justificativa
- ✅ Separação de responsabilidades
- ✅ Facilita manutenção e testes
- ✅ Apps reutilizáveis em outros projetos
- ✅ Escalabilidade (fácil adicionar novos apps)

### Consequências
- ✅ Código organizado por domínio de negócio
- ✅ Facilita testes isolados por app
- ✅ Possibilita deploy independente no futuro (microserviços)

---

## ADR-005: Uso de JWT para Autenticação

**Data:** 17/12/2025  
**Status:** ✅ Implementado  
**Decisão:** Utilizar JSON Web Tokens (JWT) via `djangorestframework-simplejwt`.

### Contexto
Aplicação frontend separada (React + Vite) requer autenticação stateless.

### Decisão
- Biblioteca: `rest_framework_simplejwt`
- Configuração em `REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES']`

### Consequências
- ✅ Autenticação stateless adequada para SPA
- ✅ Facilita escalonamento horizontal
- ✅ Tokens podem ser armazenados no frontend (localStorage/cookies)
- ✅ Refresh tokens para segurança adicional

### Referência
- Requisito: RF01 (Login via API - JWT)
- Documento: `REQUIREMENTS.MD`

---

## ADR-006: Frontend com React + Vite

**Data:** 06/01/2026  
**Status:** ✅ Implementado  
**Decisão:** Utilizar React com Vite como bundler.

### Contexto
Necessidade de framework frontend moderno para criar SPA responsiva.

### Justificativa
- ✅ **Vite:** Build ultrarrápido, HMR instantâneo
- ✅ **React:** Ecossistema maduro, componentização
- ✅ Separação clara entre frontend e backend
- ✅ Developer Experience superior

### Consequências
- ✅ Desenvolvimento frontend ágil
- ✅ Build otimizado para produção
- ✅ Hot Module Replacement instantâneo

---

## ADR-007: Tailwind CSS + shadcn/ui para Estilização

**Data:** 06/01/2026  
**Status:** ✅ Implementado  
**Decisão:** Utilizar Tailwind CSS como framework de estilização com shadcn/ui para componentes.

### Contexto
Necessidade de criar interface moderna, responsiva e com componentes reutilizáveis rapidamente.

### Decisão
- **Tailwind CSS:** Utility-first CSS framework
- **shadcn/ui:** Biblioteca de componentes React acessíveis e customizáveis

### Justificativa
- ✅ **Tailwind:** 
  - Estilização rápida com classes utilitárias
  - Design system consistente via configuração
  - Otimização automática (PurgeCSS)
  - Responsividade simplificada
  
- ✅ **shadcn/ui:**
  - Componentes acessíveis (WAI-ARIA)
  - Baseado em Radix UI (primitivos robustos)
  - Código copiado para o projeto (não é dependência)
  - Totalmente customizável via Tailwind
  - TypeScript por padrão

### Consequências

**Positivas:**
- ✅ Desenvolvimento UI acelerado
- ✅ Consistência visual automática
- ✅ Componentes prontos (botões, formulários, modais, etc.)
- ✅ Sem "vendor lock-in" (código pertence ao projeto)
- ✅ Bundle otimizado (apenas classes usadas)

**Negativas:**
- ⚠️ Curva de aprendizado do Tailwind para novos desenvolvedores
- ⚠️ HTML pode ficar verboso com muitas classes
- ⚠️ Componentes shadcn precisam ser atualizados manualmente

### Implementação
- Pasta: `frontend/src/components/ui/` (componentes shadcn)
- Configuração: `frontend/tailwind.config.js`
- Temas: `frontend/src/index.css` (variáveis CSS)

---

## ADR-008: Autenticação Obrigatória por Padrão

**Data:** 07/01/2026  
**Status:** ✅ Implementado  
**Decisão:** Configurar `IsAuthenticated` como permissão padrão para todas as views da API.

### Contexto
O sistema StockMaster gerencia informações sensíveis de estoque e produtos. Esquecimentos na configuração de permissões poderiam expor dados críticos.

### Decisão
Configurar no `settings.py`:
```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

### Consequências

**Positivas:**
- ✅ **Segurança por padrão:** Todas as views são protegidas automaticamente
- ✅ **Redução de risco humano:** Elimina possibilidade de esquecimento
- ✅ **Princípio do menor privilégio:** Acesso negado por padrão, permitido explicitamente

**Negativas:**
- ⚠️ **Explicitação necessária:** Views públicas (login, registro) precisam declarar `permission_classes = [AllowAny]` explicitamente

### Implementação
- Arquivo: `backend/config/settings.py`
- Views afetadas: Todas as ViewSets em `apps/products/views.py` e futuras views

### Referência
- Requisito: RF02 (Diferenciação de permissões)
- Documento: `REQUIREMENTS.MD`

---

## ADR-009: CORS Configurado para Desenvolvimento Local

**Data:** 17/01/2026  
**Status:** ✅ Implementado  
**Decisão:** Permitir requisições CORS do servidor Vite local.

### Contexto
Frontend React (porta 5173) precisa fazer requisições para backend Django (porta 8000).

### Configuração Atual
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
CORS_ALLOW_CREDENTIALS = True
```

### ⚠️ Ação Necessária para Produção
Antes do deploy em produção:
1. Substituir por domínio real da aplicação
2. Remover `ALLOWED_HOSTS = ["*"]`
3. Configurar variáveis de ambiente para URLs dinâmicas

---

## ADR-010: Pipeline de Qualidade e Padronização de Ambiente

**Data:** 17/01/2026  
**Status:** ✅ Implementado  
**Decisão:** Centralizar a qualidade de código e a experiência de desenvolvimento (DX) através do uso de Ruff, Pre-commit, Pytest e configurações compartilhadas do VS Code.

### Contexto
Para manter a escalabilidade e a manutenibilidade do projeto, é necessário garantir que o código siga padrões rigorosos de estilo e lógica, evitando "dívida técnica" e discussões improdutivas sobre formatação. Além disso, o ambiente de desenvolvimento deve ser consistente para qualquer colaborador.

### Decisão
- **Linter & Formatter (Python):** Utilizar o Ruff para substituir ferramentas legadas (Black, Isort, Flake8)
- **Hooks de Commit:** Implementar Pre-commit para rodar verificações automáticas antes de cada git commit
- **Testes Automatizados:** Utilizar Pytest integrado ao Django (pytest-django) para garantir a integridade da lógica de negócio
- **Ambiente (Editor):** Padronizar o VS Code via arquivos `.vscode/settings.json` e `extensions.json`

### Justificativa
- ✅ **Ruff:** Extremamente rápido (escrito em Rust), unifica múltiplas ferramentas em uma única configuração no `pyproject.toml`
- ✅ **Pre-commit:** Atua como a primeira linha de defesa, impedindo que código "sujo" entre no histórico do Git
- ✅ **DX (Developer Experience):** Configurações automáticas de format-on-save e recomendações de extensões garantem que o editor trabalhe para o desenvolvedor, não o contrário
- ✅ **Consistência:** O uso de `printWidth: 88` tanto no Ruff quanto no Prettier mantém a mesma largura de leitura em arquivos Python e JavaScript/React

### Consequências

**Positivas:**
- ✅ Código 100% padronizado automaticamente
- ✅ Redução drástica de erros simples (imports não utilizados, variáveis órfãs)
- ✅ Onboarding imediato: ao abrir o projeto, o VS Code já sugere as extensões necessárias
- ✅ Histórico de commits limpo, focado em mudanças de lógica e não em espaços em branco

**Negativas:**
- ⚠️ Exige que o desenvolvedor instale o pre-commit localmente na primeira vez
- ⚠️ O commit pode demorar alguns segundos a mais devido às verificações

### Implementação
- **Configuração Python:** `pyproject.toml` (regras E, F, I, B, DJ, RUF, UP)
- **Configuração Git:** `.pre-commit-config.yaml`
- **Configuração VS Code:**
  - `.vscode/settings.json`: Configurações de Auto-fix e Organize Imports
  - `.vscode/extensions.json`: Lista de extensões obrigatórias (Ruff, Tailwind, ESLint, Python)
- **Configuração Frontend:** `.prettierrc` (sincronizado com o limite de 88 caracteres)

---

## ADR-011: Identidade de Produtos via UUIDv7, SkuSequence e QR Code Dinâmico

**Data:** 19/01/2026  
**Status:** ✅ Atualizado  
**Decisão:** Adotar o UUIDv7 como identificador primário e fonte de dados para o QR Code, utilizando uma tabela de sequência dedicada (SkuSequence) para gerar SKUs numéricos sequenciais e imutáveis.

### Contexto
O sistema de gestão de estoque exige uma forma de identificar produtos tanto por humanos (visualmente) quanto por máquinas (leitores de QR Code). Utilizar o SKU (Stock Keeping Unit) como dado bruto do QR Code cria um acoplamento perigoso: se o SKU mudar, as etiquetas físicas tornam-se inúteis. Além disso, o uso de UUIDs aleatórios (v4) causa fragmentação de índices.

Durante o desenvolvimento, identificamos que calcular o próximo número do SKU via busca de texto (`Max("sku")`) é inseguro devido a erros lexicográficos (onde "10" pode ser lido como menor que "9" pelo banco) e riscos de concorrência (dois usuários gerando o mesmo número simultaneamente).

### Decisão
1. **Identificador Primário:** Migrar para o UUIDv7. Ele é ordenado pelo tempo, o que melhora a performance de inserção e indexação no PostgreSQL (B-tree friendly).

2. **QR Code (Abordagem Dinâmica):** O QR Code deve armazenar apenas o UUIDv7 do produto. O sistema de leitura fará um lookup no banco de dados para encontrar o item atual, permitindo que o SKU mude sem invalidar a etiqueta física.

3. **Geração de SKU (Sequencial):** Implementar um fallback automático caso o SKU não seja preenchido. O padrão será `[CAT]-[ANO]-[SEQUENCIAL]` (ex: `ELE-2026-0001`).

4. **Gerenciador de Sequência:** Utilizar uma tabela dedicada `SkuSequence` para rastrear o `last_number` por categoria e ano, garantindo integridade numérica.

5. **Controle de Concorrência:** Uso de `select_for_update()` em transações atômicas para bloquear a linha da sequência durante o incremento, impedindo duplicidade.

6. **Sanitização de Dados:** Todo SKU deve ser normalizado para remover acentos e caracteres especiais via `unicodedata`.

7. **Imutabilidade:** O SKU e o QR Code são gerados apenas na criação do registro (`is_new`), impedindo que edições posteriores alterem a identidade original.

8. **Gestão de Arquivos:** Utilizar Signals para garantir que a exclusão de um produto remova fisicamente seu arquivo de imagem do disco.

### Justificativa
- ✅ **UUIDv7:** Une unicidade global com performance de chave sequencial.
- ✅ **Desacoplamento:** O link entre objeto físico e digital torna-se eterno ao usar o ID no QR Code.
- ✅ **Confiabilidade Matemática:** A tabela de sequência garante que o próximo número será sempre +1, independente da formatação da string.
- ✅ **Segurança Multiusuário:** O bloqueio em nível de linha permite que o sistema escale sem conflitos de escrita.
- ✅ **Integridade de Storage:** A limpeza automática de arquivos evita o acúmulo de lixo eletrônico.

### Consequências

**Positivas:**
- ✅ Performance de banco de dados otimizada para grandes volumes.
- ✅ Risco zero de colisão de SKU em ambientes concorrentes.
- ✅ Etiquetas de QR Code imunes a mudanças de metadados.
- ✅ Ordenação numérica sempre correta (0001, 0002...).

**Negativas:**
- ⚠️ Exige a dependência adicional da biblioteca `uuid6`.
- ⚠️ Adiciona uma tabela extra (`SkuSequence`) ao esquema do banco.
- ⚠️ Requer reset ou migração cuidadosa do banco, pois o `id` é Primary Key.

### Implementação
- **Modelagem:** `Product.id` com `uuid6.uuid7` e `sku` com `db_index=True`.
- **Sequência:** Tabela `SkuSequence` com `unique_together` para categoria e ano.
- **Automação:** Método `save()` orquestrando `select_for_update()` e geração de imagem.
- **Infraestrutura:** Pasta `media/qrcodes/` gerenciada via Signal `post_delete`.

### Referência
- Requisito: RF04 (Geração automática de QR Code no Backend).
- Documento: `REQUIREMENTS.MD`.
- Issue: #5.

---

## Próximas Decisões a Documentar

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

*Este documento evolui com o projeto. Última atualização: 19/01/2026*
