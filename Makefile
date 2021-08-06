.PHONY: all
all: test lint

.PHONY: bootstrap
bootstrap:
	pip install -r dev-requirements.txt
	pip install -r test-requirements.txt

.PHONY: test
test:
	tox -e py39

.PHONY: lint
lint:
	tox -e lint