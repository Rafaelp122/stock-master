.PHONY: help
help:
	@echo "============================================"
	@echo "  Stock Master - Comandos Disponíveis"
	@echo "============================================"
	@echo ""
	@echo "📦 DOCKER"
	@echo "  make up          - Inicia containers, migrations e exibe logs"
	@echo "  make down        - Para todos os containers"
	@echo "  make build       - Reconstrói e inicia containers"
	@echo "  make rebuild     - Reconstrói sem cache"
	@echo "  make clean       - Remove containers, redes e volumes não usados"
	@echo ""
	@echo "🐍 BACKEND (Django)"
	@echo "  make migrate     - Aplica migrations no banco"
	@echo "  make makemigrations - Cria arquivos de migration"
	@echo "  make superuser   - Cria usuário admin"
	@echo "  make shell       - Abre shell do Django"
	@echo "  make reqs        - Atualiza requirements.txt"
	@echo ""
	@echo "⚛️  FRONTEND (React/Vite)"
	@echo "  make front-install - Instala dependências npm"
	@echo "  make front-dev   - Inicia servidor de desenvolvimento"
	@echo "  make front-build - Gera build de produção"
	@echo "  make front-sh    - Abre shell no container"
	@echo "  make front-logs  - Exibe logs do frontend"
	@echo ""
	@echo "🧹 QUALIDADE DE CÓDIGO"
	@echo "  make lint        - Verifica erros com Ruff"
	@echo "  make format      - Formata código automaticamente"
	@echo "  make test        - Executa testes com pytest"
	@echo ""
	@echo "🔧 UTILITÁRIOS"
	@echo "  make fix-perms   - Corrige permissões de arquivos"
	@echo "  make help        - Exibe esta mensagem"
	@echo ""

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

# Instala as dependências do frontend (npm install)
front-install:
	docker compose exec frontend npm install

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
