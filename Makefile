run-local:
	docker compose build
	docker compose up

stop-local:
	docker compose down
