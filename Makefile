start: stop
	docker-compose up -d

stop:
	docker-compose down

clean-volumes:
	docker-compose down -v

rebuild:
	docker-compose build --no-cache
	
test-all:
	pytest

test-unit:
	pytest -m unit

test-integration:
	pytest -m integration

loaddata:
	python manage.py loaddata $$(find . -path "*/fixtures/*.json")