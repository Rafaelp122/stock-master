# Regras de Negócio - StockMaster

Este documento define as regras de negócio fundamentais do sistema de gestão de estoque.

---

## 1. Gestão de Identidade (Módulo de Produtos)

**RN01 - Unicidade de SKU:** O SKU deve ser único em todo o sistema.

**RN02 - Imutabilidade de Identidade:** Uma vez gerado, o SKU e o QR Code de um produto não podem ser alterados, garantindo a integridade das etiquetas físicas.

**RN03 - Padronização de SKU:** SKUs automáticos devem seguir obrigatoriamente o padrão `[CATEGORIA]-[ANO]-[SEQUENCIAL]`.

---

## 2. Controle de Movimentação (Módulo de Estoque)

**RN04 - Saldo Não-Negativo:** Nenhuma operação de saída pode ser concluída se o saldo resultante for menor que zero.

**RN05 - Obrigatoriedade de Log:** Toda e qualquer alteração no saldo de um produto deve gerar um registro de movimentação (`StockMovement`) vinculado a um usuário.

**RN06 - Tipos de Movimentação:**
- **ENTRADA:** Aumenta o saldo.
- **SAÍDA:** Diminui o saldo.
- **AJUSTE:** Corrige o saldo (uso exclusivo de perfis `MANAGER`).

---

## 3. Permissões e Segurança (RBAC)

**RN07 - Hierarquia de Operações:**
- **OPERATOR:** Pode realizar Entradas e Saídas simples.
- **MANAGER:** Pode realizar Ajustes, Deletar Produtos e Visualizar logs de outros usuários.

---

*Última atualização: 20/01/2026*
