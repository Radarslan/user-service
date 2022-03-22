:: docker-compose exec user-service alembic downgrade -1
:: docker-compose exec user-service alembic revision --autogenerate -m "initial"
:: docker-compose exec user-service alembic upgrade head