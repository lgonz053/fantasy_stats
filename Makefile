ENV = $(CURDIR)/env
PIP = $(ENV)/bin/pip
PYTHON = $(ENV)/bin/python

$(ENV):
		python -m venv $(ENV)

deps: $(ENV)
		$(PIP) install -r requirements/base.txt

test-deps: deps
		$(PIP) install -r requirements/base.txt

format:
		$(ENV)/bin/black fantasy_sports/fantasy_basketball.py

check-format:
		$(ENV)/bin/black fantasy_sports/fantasy_basketball.py --check

test: test-deps
		$(PYTHON) -m unittest -v test/test_fantasy_basketball

clean:
		rm -rf $(ENV)