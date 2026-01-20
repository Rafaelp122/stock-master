# ADR-013: Padronização do Registo de Decisões Arquiteturais

**Data:** 20/01/2026  
**Status:** ✅ Implementado  

## Decisão
Adotar o padrão de ficheiros individuais para o registo de Architecture Decision Records (ADRs).

## Contexto
À medida que o sistema cresce, o ficheiro único de arquitetura torna-se denso e difícil de manter. A mistura do estado atual do design com o histórico de decisões passadas prejudica a legibilidade para novos colaboradores e a precisão do rastreio de alterações no Git.

## Decisão Técnica

1. **Armazenamento:** Cada ADR deve ser guardada como um ficheiro Markdown individual no diretório `docs/adr/`, seguindo a nomenclatura `XXXX-titulo-da-decisao.md`.

2. **Índice:** O ficheiro `ARCHITECTURE.md` na raiz da pasta `docs/` passa a servir como a "Fonte da Verdade" para o estado atual do sistema, contendo um índice que aponta para as ADRs individuais.

3. **Processo:** Novas decisões devem ser propostas como um novo ficheiro na pasta de ADRs e, após aprovação/implementação, o índice no ficheiro principal deve ser atualizado.

## Justificativa
- ✅ **Rastreabilidade:** Permite identificar exatamente quando e por que uma decisão específica foi alterada através do histórico do ficheiro.
- ✅ **Modularidade:** Facilita a referência a decisões específicas em outras Issues ou Pull Requests através de links diretos.
- ✅ **Manutenibilidade:** O mapa da arquitetura atual permanece limpo, enquanto o histórico cresce de forma organizada em ficheiros separados.

## Consequências

### Positivas
- ✅ Organização de nível profissional
- ✅ Histórico do Git mais limpo e preciso
- ✅ Facilidade de navegação e referência
- ✅ Melhor experiência para novos colaboradores

### Negativas
- ⚠️ Requer um pequeno esforço adicional para manter o índice do `ARCHITECTURE.md` atualizado com os novos ficheiros
- ⚠️ Necessita de disciplina da equipa para seguir o padrão estabelecido

## Implementação
- **Estrutura:** `docs/adr/XXXX-titulo.md`
- **Índice:** `docs/ARCHITECTURE.md` (resumo executivo)
- **Guia:** `docs/adr/README.md` (template e instruções)

## Referência
- Issue: #16
