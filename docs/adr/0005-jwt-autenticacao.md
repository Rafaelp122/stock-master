# ADR-005: Uso de JWT para Autenticação

**Data:** 17/12/2025  
**Status:** ✅ Implementado  

## Decisão
Utilizar JSON Web Tokens (JWT) via `djangorestframework-simplejwt`.

## Contexto
Aplicação frontend separada (React + Vite) requer autenticação stateless.

## Decisão Técnica
- Biblioteca: `rest_framework_simplejwt`
- Configuração em `REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES']`

## Consequências
- ✅ Autenticação stateless adequada para SPA
- ✅ Facilita escalonamento horizontal
- ✅ Tokens podem ser armazenados no frontend (localStorage/cookies)
- ✅ Refresh tokens para segurança adicional

## Referência
- Requisito: RF01 (Login via API - JWT)
- Documento: `REQUIREMENTS.MD`
