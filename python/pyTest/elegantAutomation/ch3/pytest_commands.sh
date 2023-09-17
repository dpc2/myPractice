pytest -m smoke
pytest -m body
pytest -m "body engine"
pytest -m "body and engine"
pytest -m "not entertainment"
pytest -m "not ui"
pytest -m "backend not ui"

# List markers
pytest --markers

