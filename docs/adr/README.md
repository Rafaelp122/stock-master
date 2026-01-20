# Architecture Decision Records (ADR)

Este diretório contém as decisões arquiteturais do projeto StockMaster.

## Índice de ADRs

- [ADR-001: Uso de Docker para Containerização](0001-uso-do-docker.md)
- [ADR-002: Definição de Stack Tecnológica](0002-stack-tecnologica.md)
- [ADR-003: Uso de Makefile para Automação de Tarefas](0003-uso-do-makefile.md)
- [ADR-004: Estrutura de Apps Django](0004-estrutura-de-apps-django.md)
- [ADR-005: Uso de JWT para Autenticação](0005-jwt-autenticacao.md)
- [ADR-006: Frontend com React + Vite](0006-frontend-react-vite.md)
- [ADR-007: Tailwind CSS + shadcn/ui para Estilização](0007-tailwind-shadcn.md)
- [ADR-008: Autenticação Obrigatória por Padrão](0008-autenticacao-obrigatoria.md)
- [ADR-009: CORS Configurado para Desenvolvimento Local](0009-cors-desenvolvimento.md)
- [ADR-010: Pipeline de Qualidade e Padronização de Ambiente](0010-pipeline-qualidade.md)
- [ADR-011: Identidade de Produtos via UUIDv7, SkuSequence e QR Code Dinâmico](0011-identidade-produtos-uuidv7.md)
- [ADR-012: Restrição de Acesso aos Arquivos de Mídia](0012-restricao-acesso-media.md)
- [ADR-013: Padronização do Registo de Decisões Arquiteturais](0013-padronizacao-registro-adr.md)

## Status das ADRs

- ✅ **Implementado:** Decisão já aplicada no projeto
- 🏗️ **Proposto:** Decisão planejada, aguardando implementação
- ❌ **Rejeitado:** Decisão considerada e rejeitada
- 🔄 **Substituído:** Substituída por uma ADR mais recente

## Como Criar uma Nova ADR

1. Crie um novo arquivo seguindo o padrão: `XXXX-titulo-da-decisao.md`
2. Use o próximo número sequencial disponível
3. Siga o template padrão com as seções: Data, Status, Decisão, Contexto, Justificativa, Consequências, Implementação e Referência
4. Atualize este README.md adicionando a nova ADR ao índice
5. Atualize a data no `ARCHITECTURE.md`

## Template de ADR

```markdown
# ADR-XXX: Título da Decisão

**Data:** DD/MM/AAAA  
**Status:** ✅ Implementado / 🏗️ Proposto / ❌ Rejeitado / 🔄 Substituído  

## Decisão
[Decisão tomada em uma linha]

## Contexto
[Por que essa decisão foi necessária?]

## Decisão Técnica
[Detalhes técnicos da implementação]

## Justificativa
[Por que essa foi a melhor escolha?]

## Consequências

### Positivas
[Benefícios da decisão]

### Negativas
[Trade-offs e limitações]

## Implementação
[Onde e como foi implementado]

## Referência
[Links para issues, requisitos, documentos relacionados]
```

---

*Última atualização: 20/01/2026*
