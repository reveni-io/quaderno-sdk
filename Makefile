tests ?= tests

init.test:
	@pip install -r requirements/tests.txt

init.dist:
	@pip install -r requirements/dist.txt

init: init.test init.dist
	@pip install -r requirements/base.txt

test:
	@$(PYTEST) --verbose $(tests)

coverage:
	@$(PYTEST) --verbose --cov-report term --cov=quaderno_sdk $(tests)
	@coveralls
