tests ?= tests

init.test:
	@pip install -r requirements/tests.txt

init.dist:
	@pip install -r requirements/dist.txt

init: init.test init.dist
	@pip install -r requirements/local.txt

test:
	@$(PYTEST) --verbose $(tests)

coverage:
	@$(PYTEST) --verbose --cov-report term --cov=aplazame_sdk $(tests)
	@coveralls
