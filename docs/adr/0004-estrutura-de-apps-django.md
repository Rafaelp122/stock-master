# ADR-004: Estrutura de Apps Django

**Data:** 14/12/2025  
**Status:** ✅ Implementado  

## Decisão
Organizar código em apps Django separados por domínio.

## Contexto
Necessidade de estruturar o backend de forma modular e escalável.

## Estrutura
```
backend/apps/
├── users/      # Gestão de usuários e autenticação
└── products/   # Produtos, categorias e estoque
```

## Justificativa
- ✅ Separação de responsabilidades
- ✅ Facilita manutenção e testes
- ✅ Apps reutilizáveis em outros projetos
- ✅ Escalabilidade (fácil adicionar novos apps)

## Consequências
- ✅ Código organizado por domínio de negócio
- ✅ Facilita testes isolados por app
- ✅ Possibilita deploy independente no futuro (microserviços)
