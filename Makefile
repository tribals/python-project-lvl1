install:
	poetry install

.PHONY: install

brain-games:
	poetry run brain-games

.PHONY: brain-games

brain-even:
	poetry run brain-even

.PHONY: brain-even

dist/hexlet_code-*-py3-none-any.whl: brain_games/**/*.py
	poetry build --format wheel

build: dist/hexlet_code-*-py3-none-any.whl

lint:
	poetry run flake8 brain_games

.PHONY: lint

clean:
	rm -r dist/

.PHONY: clean

publish:
	poetry publish --dry-run

.PHONY: publish

package-install: build
	python3 -m pip install --force-reinstall --user dist/hexlet_code-*-py3-none-any.whl
