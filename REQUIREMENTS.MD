# StockMaster - Requisitos do Sistema

## Módulo 1: Autenticação
- [ ] **RF01:** Login via API (JWT - SimpleJWT).
- [ ] **RF02:** Diferenciação de permissões (Admin vs Operador).

## Módulo 2: Gestão de Produtos
- [ ] **RF03:** CRUD de Produtos (Criar, Listar, Editar, Desativar).
- [ ] **RF04:** Geração automática de QR Code no Backend (Python).
- [ ] **RF05:** Alerta de Estoque Mínimo no Dashboard.

## Módulo 3: Movimentação (Core)
- [ ] **RF06:** Entrada de Estoque (Aumentar quantidade).
- [ ] **RF07:** Saída de Estoque (Diminuir quantidade).
- [ ] **RF08:** Validação de Saldo (Impedir saída se estoque < 0).
- [ ] **RF09:** Histórico de Movimentações (Log de quem fez e quando).

## Módulo 4: Interface (React)
- [ ] **RF10:** Leitura de QR Code via Câmera (Mobile/Web).

## Stack Tecnológica (RNF)
- Backend: Django Rest Framework + PostgreSQL + Docker.
- Frontend: React (Vite) + TailwindCSS.
- Autenticação: SimpleJWT.