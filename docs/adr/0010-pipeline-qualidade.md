# ADR-010: Pipeline de Qualidade e Padronização de Ambiente

**Data:** 17/01/2026  
**Status:** ✅ Implementado  

## Decisão
Centralizar a qualidade de código e a experiência de desenvolvimento (DX) através do uso de Ruff, Pre-commit, Pytest e configurações compartilhadas do VS Code.

## Contexto
Para manter a escalabilidade e a manutenibilidade do projeto, é necessário garantir que o código siga padrões rigorosos de estilo e lógica, evitando "dívida técnica" e discussões improdutivas sobre formatação. Além disso, o ambiente de desenvolvimento deve ser consistente para qualquer colaborador.

## Decisão Técnica
- **Linter & Formatter (Python):** Utilizar o Ruff para substituir ferramentas legadas (Black, Isort, Flake8)
- **Hooks de Commit:** Implementar Pre-commit para rodar verificações automáticas antes de cada git commit
- **Testes Automatizados:** Utilizar Pytest integrado ao Django (pytest-django) para garantir a integridade da lógica de negócio
- **Ambiente (Editor):** Padronizar o VS Code via arquivos `.vscode/settings.json` e `extensions.json`

## Justificativa
- ✅ **Ruff:** Extremamente rápido (escrito em Rust), unifica múltiplas ferramentas em uma única configuração no `pyproject.toml`
- ✅ **Pre-commit:** Atua como a primeira linha de defesa, impedindo que código "sujo" entre no histórico do Git
- ✅ **DX (Developer Experience):** Configurações automáticas de format-on-save e recomendações de extensões garantem que o editor trabalhe para o desenvolvedor, não o contrário
- ✅ **Consistência:** O uso de `printWidth: 88` tanto no Ruff quanto no Prettier mantém a mesma largura de leitura em arquivos Python e JavaScript/React

## Consequências

### Positivas
- ✅ Código 100% padronizado automaticamente
- ✅ Redução drástica de erros simples (imports não utilizados, variáveis órfãs)
- ✅ Onboarding imediato: ao abrir o projeto, o VS Code já sugere as extensões necessárias
- ✅ Histórico de commits limpo, focado em mudanças de lógica e não em espaços em branco

### Negativas
- ⚠️ Exige que o desenvolvedor instale o pre-commit localmente na primeira vez
- ⚠️ O commit pode demorar alguns segundos a mais devido às verificações

## Implementação
- **Configuração Python:** `pyproject.toml` (regras E, F, I, B, DJ, RUF, UP)
- **Configuração Git:** `.pre-commit-config.yaml`
- **Configuração VS Code:**
  - `.vscode/settings.json`: Configurações de Auto-fix e Organize Imports
  - `.vscode/extensions.json`: Lista de extensões obrigatórias (Ruff, Tailwind, ESLint, Python)
- **Configuração Frontend:** `.prettierrc` (sincronizado com o limite de 88 caracteres)
