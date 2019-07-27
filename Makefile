ENV = $(CURDIR)/env

$(ENV):
				python -m venv $(ENV)

format:
				$(ENV)/bin/black fantasy_basketball.py