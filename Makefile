.PHONY: run build run-docker

# Local development
run:
	.\venv\Scripts\activate
	uvicorn backend.main:app --reload

# Docker
build:
	docker build -t palmer .

run-docker:
	docker run -p 8000:8000 --env-file .env palmer
