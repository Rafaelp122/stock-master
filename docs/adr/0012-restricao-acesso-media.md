# ADR-012: Restrição de Acesso aos Arquivos de Mídia

**Data:** 20/01/2026  
**Status:** 🏗️ Proposto (Issue #15)  

## Decisão
Não servir QR Codes como arquivos estáticos públicos; utilizar uma View protegida com FileResponse.

## Contexto
Arquivos na pasta `/media/` são públicos por padrão no Django. Qualquer pessoa com o link do QR Code poderia visualizar a etiqueta de um produto interno.

## Decisão Técnica
1. Criar rota `/api/products/media/qrcode/<uuid:id>/` protegida por `IsAuthenticated`.
2. O Django lerá o arquivo do disco e o entregará via `FileResponse` apenas para usuários logados.

## Justificativa
- ✅ **Privacidade:** Impede que links de imagens vazem para fora da empresa.
- ✅ **Controle:** Permite auditar quem está visualizando os arquivos.

## Consequências

### Positivas
- ✅ Segurança adicional para arquivos sensíveis
- ✅ Possibilidade de auditoria de acesso a imagens
- ✅ Controle granular de permissões por arquivo

### Negativas
- ⚠️ Overhead de processamento (Django serve o arquivo ao invés do nginx/servidor web)
- ⚠️ Necessário atualizar frontend para incluir token de autenticação nas requisições de imagem

## Referência
- Issue: #15
