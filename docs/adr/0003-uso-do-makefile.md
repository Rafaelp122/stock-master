# ADR-003: Uso de Makefile para Automação de Tarefas

**Data:** 14/12/2025  
**Status:** ✅ Implementado  

## Decisão
Utilizar Makefile para padronizar e simplificar comandos do projeto.

## Contexto
Comandos Docker e Django podem ser longos e difíceis de memorizar. Necessidade de padronizar tarefas comuns entre desenvolvedores.

## Decisão Técnica
Criar `Makefile` na raiz do projeto com comandos simplificados.

## Justificativa
- ✅ **Simplicidade:** `make up` ao invés de `docker-compose up -d`
- ✅ **Documentação viva:** Makefile serve como referência de comandos disponíveis
- ✅ **Onboarding:** Novos desenvolvedores aprendem comandos rapidamente
- ✅ **Consistência:** Todos executam comandos da mesma forma
- ✅ **Produtividade:** Reduz tempo digitando comandos complexos

## Comandos Principais
```makefile
make up          # Sobe os containers
make down        # Derruba os containers
make logs        # Mostra logs
make migrate     # Executa migrações
make shell       # Acessa shell do Django
make test        # Executa testes
make format      # Formata código (black, isort)
```

## Consequências

### Positivas
- ✅ Reduz erros de digitação em comandos
- ✅ Facilita automação de CI/CD (make test, make deploy)
- ✅ Documentação centralizada de tarefas

### Negativas
- ⚠️ Desenvolvedores precisam ter `make` instalado (padrão em Linux/Mac, precisa instalar no Windows)
- ⚠️ Mais uma ferramenta para aprender (curva pequena)

## Implementação
- Arquivo: `Makefile` (raiz do projeto)
- Compatibilidade: Linux, macOS, Windows (via Git Bash ou WSL)
