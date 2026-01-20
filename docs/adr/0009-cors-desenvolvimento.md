# ADR-009: CORS Configurado para Desenvolvimento Local

**Data:** 17/01/2026  
**Status:** ✅ Implementado  

## Decisão
Permitir requisições CORS do servidor Vite local.

## Contexto
Frontend React (porta 5173) precisa fazer requisições para backend Django (porta 8000).

## Configuração Atual
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
CORS_ALLOW_CREDENTIALS = True
```

## ⚠️ Ação Necessária para Produção
Antes do deploy em produção:
1. Substituir por domínio real da aplicação
2. Remover `ALLOWED_HOSTS = ["*"]`
3. Configurar variáveis de ambiente para URLs dinâmicas
