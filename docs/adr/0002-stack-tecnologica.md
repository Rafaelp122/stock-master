# ADR-002: Definição de Stack Tecnológica

**Data:** 14/12/2025  
**Status:** ✅ Implementado  

## Decisão
Stack baseada em Django REST Framework + React + PostgreSQL.

## Contexto
Necessidade de escolher tecnologias maduras, escaláveis e com boa comunidade para um sistema de gestão de estoque.

## Decisão Técnica
- **Backend:** Django REST Framework (Python)
- **Frontend:** React com Vite
- **Banco de Dados:** PostgreSQL
- **Autenticação:** JWT (SimpleJWT)

## Justificativa

### Backend - Django REST Framework
- ✅ Framework maduro e bem documentado
- ✅ ORM poderoso (abstração de banco de dados)
- ✅ Admin panel nativo
- ✅ Ecossistema rico (bibliotecas para QR Code, exportação, etc.)
- ✅ Segurança built-in (CSRF, SQL injection, XSS)

### Frontend - React
- ✅ Biblioteca mais popular para SPAs
- ✅ Componentização reutilizável
- ✅ Vite para build ultrarrápido
- ✅ Ecossistema maduro (routing, state management, etc.)

### Banco de Dados - PostgreSQL
- ✅ Robusto para produção
- ✅ Suporte a JSON (flexibilidade futura)
- ✅ Integridade referencial
- ✅ Open-source

## Consequências
- ✅ Stack moderna e escalável
- ✅ Separação clara frontend/backend (arquitetura desacoplada)
- ✅ Facilita contratação (tecnologias populares)

## Referência
- Documento: `REQUIREMENTS.MD` (Stack Tecnológica - RNF)
