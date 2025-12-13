PYTHON?=${VIRTUAL_ENV}/bin/python

.PHONY: venv install dev lint format test cov

venv:
	python3 -m venv projects/01-web-scraper/venv

install:
	. projects/01-web-scraper/venv/bin/activate && pip install -r projects/01-web-scraper/requirements.txt

dev:
	. projects/01-web-scraper/venv/bin/activate && pip install pytest pytest-cov black ruff

lint:
	. projects/01-web-scraper/venv/bin/activate && ruff check .

format:
	. projects/01-web-scraper/venv/bin/activate && black . && ruff format .

test:
	. projects/01-web-scraper/venv/bin/activate && pytest

cov:
	. projects/01-web-scraper/venv/bin/activate && pytest --cov=projects/01-web-scraper --cov-report=term-missing
