# Comandos do Docker
up:
	docker compose up

down:
	docker compose down

build:
	docker compose up --build

# Comandos do Django (Backend)
migrate:
	docker compose exec backend python manage.py migrate

makemigrations:
	docker compose exec backend python manage.py makemigrations

superuser:
	docker compose exec backend python manage.py createsuperuser

shell:
	docker compose exec backend python manage.py shell

# Utilitários de Sistema
fix-perms:
	sudo chown -R $$USER:$$USER .

# Frontend e Utilitários
front-sh:
	docker compose exec frontend sh

front-logs:
	docker compose logs -f frontend

test:
	docker compose exec backend pytest
