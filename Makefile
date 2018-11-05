SHELL := /bin/bash
MAKEFLAGS += --warn-undefined-variables
SHELL := /bin/bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := ci
.DELETE_ON_ERROR:
.SUFFIXES:

BUILD_VERSION?=$(shell tail -n 1 airswap_exercise/__init__.py | sed -r 's/.*([0-9]+\.[0-9]+\.[0-9]).*/\1/')

SRC := $(shell find airswap_exercise -type f -name '*.py')


ARTIFACT_DIR := artifacts/
PEP8_CONFIG := .pep8
PEP8_REPORT := $(ARTIFACT_DIR)checkstyle/pep8.log
PYFLAKES_REPORT := $(ARTIFACT_DIR)checkstyle/pyflakes.log
TEST_DIR := tests/
TEST_REPORT := $(ARTIFACT_DIR)test/report.xml
COVERAGE_REPORT := $(ARTIFACT_DIR)coverage/coverage.xml
PEP8_PYTHON2_COMPAT := $(shell /usr/bin/which pep8-python2)

ifneq ("$(wildcard $(PEP8_PYTHON2_COMPAT))","")
	PEP8_BIN := pep8-python2
else
	PEP8_BIN := pep8
endif

PYFLAKES_PYTHON2_COMPAT := $(shell /usr/bin/which pyflakes-python2)

ifneq ("$(wildcard $(pyflakes_python2_compat))","")
	PYFLAKES_BIN := pyflakes-python2
else
	PYFLAKES_BIN := pyflakes
endif

PYTEST_BIN := py.test

$(PEP8_REPORT): $(SRC)
	@mkdir -p $(dir $@)
	@$(PEP8_BIN) --config=$(PEP8_CONFIG) $^ > $@ || true

$(PYFLAKES_REPORT): $(SRC)
	@mkdir -p $(dir $@)
	@$(PYFLAKES_BIN) $^ > $@ || true

$(TEST_REPORT) $(COVERAGE_REPORT): $(SRC)
	@mkdir -p $(dir $(TEST_REPORT))
	@mkdir -p $(dir $(COVERAGE_REPORT))
	@$(PYTEST_BIN) --cov-report xml --cov=. $(TEST_DIR) --junitxml=$(TEST_REPORT) || true

.PHONY: test
test: $(PEP8_REPORT) $(PYFLAKES_REPORT) $(COVERAGE_REPORT)

.PHONY: snapshot
snapshot: test


.PHONY: release
release: snapshot


.PHONY: clean
clean:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*.cache' -exec rm -rf {} +
	@find . -name '*.coverage' -exec rm -rf {} +
	@find . -name '__pycache__' -exec rm -rf {} +
	@find . -name '*~' -exec rm -f {} +
	@rm -rf $(ARTIFACT_DIR)

