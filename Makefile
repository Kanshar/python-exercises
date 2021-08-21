setup:
	python3 -m venv venv

install:
	python3 -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --upgrade pip && \
	pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org  -r requirements.txt

lint:
	python3 -m pylint profit.py

test:
	python3 -m pytest -vv --cov=profit -q tests/*.py

all: install lint test