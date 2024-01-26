# Makefile

api:
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

createsuperuser_dev:
	python manage.py createsuperuser_dev --username dev_user --password dev_user --email 'dev@user.com' --no-input --preserve

clean-redis:
	docker exec -it $$(docker ps -aqf "name=mb-crypto-cache") redis-cli FLUSHALL

help:
	@echo "Usage:"
	@echo "  make api                 : Start the Docker containers in detached mode"
	@echo "  make stop                : Stop the Docker containers"
	@echo "  make clean-volumes       : Stop the containers and remove associated volumes"
	@echo "  make rebuild             : Rebuild Docker containers without using cache"
	@echo "  make test-all            : Run all tests"
	@echo "  make test-unit           : Run unit tests"
	@echo "  make test-integration    : Run integration tests"
	@echo "  make loaddata            : Load fixture data into the application"
	@echo "  make createsuperuser_dev : Create a development superuser"
	@echo "  make clean-redis         : Deletes all cached keys in the Redis database"
