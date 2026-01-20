# ADR-008: Autenticação Obrigatória por Padrão

**Data:** 07/01/2026  
**Status:** ✅ Implementado  

## Decisão
Configurar `IsAuthenticated` como permissão padrão para todas as views da API.

## Contexto
O sistema StockMaster gerencia informações sensíveis de estoque e produtos. Esquecimentos na configuração de permissões poderiam expor dados críticos.

## Decisão Técnica
Configurar no `settings.py`:
```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

## Consequências

### Positivas
- ✅ **Segurança por padrão:** Todas as views são protegidas automaticamente
- ✅ **Redução de risco humano:** Elimina possibilidade de esquecimento
- ✅ **Princípio do menor privilégio:** Acesso negado por padrão, permitido explicitamente

### Negativas
- ⚠️ **Explicitação necessária:** Views públicas (login, registro) precisam declarar `permission_classes = [AllowAny]` explicitamente

## Implementação
- Arquivo: `backend/config/settings.py`
- Views afetadas: Todas as ViewSets em `apps/products/views.py` e futuras views

## Referência
- Requisito: RF02 (Diferenciação de permissões)
- Documento: `REQUIREMENTS.MD`
