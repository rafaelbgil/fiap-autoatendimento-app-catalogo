test:
	coverage run --source=./src -m unittest discover -s tests/domain/entities/
	coverage html

run:
	uvicorn src.web.main:app --reload


