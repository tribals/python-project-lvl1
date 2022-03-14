.PHONY: install
install:
	poetry install

.PHONY: brain-games
brain-games:
	poetry run brain-games

.PHONY: brain-even
brain-even:
	poetry run brain-even

.PHONY: brain-calc
brain-calc:
	poetry run brain-calc

.PHONY: brain-gcd
brain-gcd:
	poetry run brain-gcd

dist/hexlet_code-*-py3-none-any.whl: brain_games/**/*.py
	poetry build --format wheel

build: dist/hexlet_code-*-py3-none-any.whl

.PHONY: lint
lint:
	poetry run flake8 brain_games

.PHONY: clean
clean:
	rm -r dist/

.PHONY: publish
publish:
	poetry publish --dry-run

package-install: build
	python3 -m pip install --force-reinstall --user dist/hexlet_code-*-py3-none-any.whl
