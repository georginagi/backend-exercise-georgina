.PHONY: build
build:
	docker-compose build
dockerize: build
	@docker build -t nextail:latest .

start: build
	docker-compose up

stop:
	docker-compose down -v

shell: build
	docker-compose run nextail sh

test: build
	docker-compose run nextail mamba -f documentation test/unit/
