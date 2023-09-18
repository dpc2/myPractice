# Install commands
pip install pytest
pip install pytest-xdist

pytest -m smoke
pytest -m body
pytest -m "body engine"
pytest -m "body and engine"
pytest -m "not entertainment"
pytest -m "not ui"
pytest -m "backend not ui"

# List markers
pytest --markers

# Using custom terminal options
pytest --env dev -v
# Skip and Xfail
pytest --env dev -v -rs
pytest --env dev -v -rx
# Show terminal output
pytest -s

# Run parallel tests
pytest -v -s -n4
pytest -v -s -nauto