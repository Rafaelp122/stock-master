# ADR-007: Tailwind CSS + shadcn/ui para Estilização

**Data:** 06/01/2026  
**Status:** ✅ Implementado  

## Decisão
Utilizar Tailwind CSS como framework de estilização com shadcn/ui para componentes.

## Contexto
Necessidade de criar interface moderna, responsiva e com componentes reutilizáveis rapidamente.

## Decisão Técnica
- **Tailwind CSS:** Utility-first CSS framework
- **shadcn/ui:** Biblioteca de componentes React acessíveis e customizáveis

## Justificativa

### Tailwind
- ✅ Estilização rápida com classes utilitárias
- ✅ Design system consistente via configuração
- ✅ Otimização automática (PurgeCSS)
- ✅ Responsividade simplificada

### shadcn/ui
- ✅ Componentes acessíveis (WAI-ARIA)
- ✅ Baseado em Radix UI (primitivos robustos)
- ✅ Código copiado para o projeto (não é dependência)
- ✅ Totalmente customizável via Tailwind
- ✅ TypeScript por padrão

## Consequências

### Positivas
- ✅ Desenvolvimento UI acelerado
- ✅ Consistência visual automática
- ✅ Componentes prontos (botões, formulários, modais, etc.)
- ✅ Sem "vendor lock-in" (código pertence ao projeto)
- ✅ Bundle otimizado (apenas classes usadas)

### Negativas
- ⚠️ Curva de aprendizado do Tailwind para novos desenvolvedores
- ⚠️ HTML pode ficar verboso com muitas classes
- ⚠️ Componentes shadcn precisam ser atualizados manualmente

## Implementação
- Pasta: `frontend/src/components/ui/` (componentes shadcn)
- Configuração: `frontend/tailwind.config.js`
- Temas: `frontend/src/index.css` (variáveis CSS)
