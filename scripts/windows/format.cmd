isort --force-single-line-imports .;
black .;
autoflake8 ^
  --recursive ^
  --remove-unused-variables ^
  --in-place . ^
  --exclude=__init__.py,venv,.venv,.pytest_cache;
