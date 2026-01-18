.PHONY: help
help:
	@echo "=========================================================================="
	@echo "  🚀 Stock Master - Sistema de Gestão de Estoque Profissional"
	@echo "=========================================================================="
	@echo ""
	@echo "📦 DOCKER & ORQUESTRAÇÃO"
	@echo "  make up               - Inicia containers, migrations e exibe logs"
	@echo "  make down             - Para e remove todos os containers"
	@echo "  make build            - Reconstrói as imagens e inicia"
	@echo "  make rebuild          - Reconstrói as imagens do zero (sem cache)"
	@echo "  make clean            - Limpeza total (containers, volumes, redes)"
	@echo ""
	@echo "🐍 BACKEND (Django REST Framework)"
	@echo "  make migrate          - Aplica migrações no banco de dados"
	@echo "  make makemigrations   - Gera novos arquivos de migração"
	@echo "  make superuser        - Cria usuário administrativo"
	@echo "  make shell            - Acessa o shell interativo do Django"
	@echo "  make reqs             - Atualiza o arquivo requirements.txt"
	@echo ""
	@echo "⚛️  FRONTEND (React + Vite)"
	@echo "  make front-install    - Instala deps (use pkg=nome para pacotes novos)"
	@echo "  make front-dev        - Inicia o servidor local do Vite"
	@echo "  make front-build      - Gera o build de produção"
	@echo "  make front-sh         - Acessa o terminal dentro do container"
	@echo "  make front-logs       - Exibe logs específicos do frontend"
	@echo ""
	@echo "🧹 QUALIDADE & PADRONIZAÇÃO (ADR-010)"
	@echo "  make lint             - Analisa o código com Ruff"
	@echo "  make format           - Formata o código (Ruff + Prettier)"
	@echo "  make test             - Roda a bateria de testes com Pytest"
	@echo ""
	@echo "🔧 UTILITÁRIOS"
	@echo "  make fix-perms        - Corrige permissões de arquivos (Linux/macOS)"
	@echo "  make help             - Exibe este menu de ajuda"
	@echo "=========================================================================="

# Comandos do Docker
# Inicia os containers em background, roda migrations e exibe logs
up:
	docker compose up -d
	$(MAKE) migrate
	docker compose logs -f

# Para todos os containers
down:
	docker compose down

# Reconstrói e inicia os containers, roda migrations e exibe logs
build:
	docker compose up --build -d
	$(MAKE) migrate
	docker compose logs -f

# Reconstrói as imagens do zero, sem usar cache
rebuild:
	docker compose build --no-cache
	docker compose up -d
	$(MAKE) migrate
	docker compose logs -f

# Remove containers, redes e volumes que não estão sendo usados
clean:
	docker compose down -v
	docker system prune -f

# Comandos do Django (Backend)
# Aplica migrations pendentes no banco de dados
migrate:
	docker compose exec backend python manage.py migrate

# Cria novos arquivos de migration baseado nas mudanças dos models
makemigrations:
	docker compose exec backend python manage.py makemigrations

# Cria um usuário administrador para acessar o Django Admin
superuser:
	docker compose exec backend python manage.py createsuperuser

# Abre o shell interativo do Django (para testar código Python)
shell:
	docker compose exec backend python manage.py shell

# Atualiza o arquivo requirements.txt com o que está no container
# Corrige permissões de arquivos (útil quando Docker cria arquivos como root)
reqs:
	docker compose exec backend pip freeze > backend/requirements.txt

# Utilitários de Sistema
fix-perms:
	sudo chown -R $$USER:$$USER .

# Abre shell interativo no container do frontend
front-sh:
	docker compose exec frontend sh

# Exibe logs do container do frontend em tempo real
front-logs:
	docker compose logs -f frontend

# Se você rodar 'make front-install', ele instala tudo.
# Se rodar 'make front-install pkg=axios', ele instala só o axios.
front-install:
	docker compose exec frontend npm install $(pkg)

# Gera build de produção do frontend (CSS/JS otimizados na pasta dist/)
front-build:
	docker compose exec frontend npm run build

# Inicia servidor de desenvolvimento do frontend com hot reload (localhost:5173)
front-dev:
	docker compose exec frontend npm run dev

# Verifica erros de código com Ruff (linter)
lint:
	docker compose exec backend ruff check .

# Formata o código automaticamente e corrige problemas que podem ser arrumados
format:
	docker compose exec backend ruff format .
	docker compose exec backend ruff check . --fix

# Executa os testes automatizados com pytest
test:
	docker compose exec backend pytest
