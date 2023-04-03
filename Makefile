# poetry add nome_da_dependencia
# poetry install
# poetry run nome_do_comando

poetry-build:
	poetry build

poetry-publish:
	poetry publish --build

poetry-publish-testpypi:
	poetry publish --build --repository testpypi
