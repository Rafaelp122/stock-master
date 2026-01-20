# ADR-001: Uso de Docker para Containerização

**Data:** 14/12/2025  
**Status:** ✅ Implementado  

## Decisão
Utilizar Docker e Docker Compose para containerização do ambiente de desenvolvimento e produção.

## Contexto
Necessidade de garantir consistência entre ambientes de desenvolvimento, homologação e produção, além de facilitar onboarding de novos desenvolvedores.

## Decisão Técnica
- **Docker:** Containerização de aplicações (backend, frontend, banco de dados)
- **Docker Compose:** Orquestração local dos serviços

## Justificativa
- ✅ **Consistência:** "Funciona na minha máquina" = funciona em produção
- ✅ **Isolamento:** Dependências isoladas por container
- ✅ **Onboarding rápido:** `docker-compose up` e ambiente pronto
- ✅ **PostgreSQL:** Facilita uso de banco de dados em desenvolvimento
- ✅ **Deploy simplificado:** Mesma estrutura para produção

## Consequências

### Positivas
- ✅ Ambiente padronizado para toda a equipe
- ✅ Fácil reset do ambiente (volumes Docker)
- ✅ Preparação para deploy em cloud (AWS ECS, Google Cloud Run, etc.)

### Negativas
- ⚠️ Curva de aprendizado para desenvolvedores sem experiência com Docker
- ⚠️ Overhead de recursos (memória/CPU) vs ambiente nativo

## Implementação
- Arquivo: `docker-compose.yml` (raiz do projeto)
- Containers: backend (Django), frontend (React/Vite), db (PostgreSQL)
