install:
	poetry install

.PHONY: install

brain-games:
	poetry run brain-games

.PHONY: brain-games

dist/hexlet_code-*-py3-none-any.whl:
	poetry build --format wheel

build: dist/hexlet_code-*-py3-none-any.whl

clean:
	rm -r dist/

.PHONY: clean

publish:
	poetry publish --dry-run

.PHONY: publish

package-install: build
	python3 -m pip install --user dist/hexlet_code-*-py3-none-any.whl
