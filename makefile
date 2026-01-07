# Comandos do Docker
up:
	docker compose up -d
	$(MAKE) migrate
	docker compose logs -f

down:
	docker compose down

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
migrate:
	docker compose exec backend python manage.py migrate

makemigrations:
	docker compose exec backend python manage.py makemigrations

superuser:
	docker compose exec backend python manage.py createsuperuser

shell:
	docker compose exec backend python manage.py shell

# Atualiza o arquivo requirements.txt com o que está no container
reqs:
	docker compose exec backend pip freeze > backend/requirements.txt

# Utilitários de Sistema
fix-perms:
	sudo chown -R $$USER:$$USER .

# Frontend e Utilitários
front-sh:
	docker compose exec frontend sh

front-logs:
	docker compose logs -f frontend

# Qualidade de Código
lint:
	docker compose exec backend ruff check .

format:
	docker compose exec backend ruff format .
	docker compose exec backend ruff check . --fix

test:
	docker compose exec backend pytest
