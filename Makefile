all:
	@make down
	@make clean-build
	@make up

build:
	@docker-compose -f docker-compose.yml build

clean-build:
	@docker-compose -f docker-compose.yml build --no-cache

up:
	@docker-compose -f docker-compose.yml up -d

down:
	@docker-compose -f docker-compose.yml down

stop:
	@docker-compose -f docker-compose.yml stop

restart:
	@docker-compose -f docker-compose.yml stop
	@docker-compose -f docker-compose.yml up -d

