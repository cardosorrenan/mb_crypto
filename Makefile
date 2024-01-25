

loaddata:
	python manage.py loaddata $$(find . -path "*/fixtures/*.json")
