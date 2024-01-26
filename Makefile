start: stop
	docker-compose up -d

stop:
	docker-compose down

test-all:
	pytest

test-unit:
	pytest -m unit

test-integration:
	pytest -m integration

loaddata:
	python manage.py loaddata $$(find . -path "*/fixtures/*.json")