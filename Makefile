app_name = flask-url-shortener-app
host_port = 8000

build:
	@docker build -t $(app_name) .

run:
	@docker run -p 8000:$(host_port) $(app_name)

run-detach:
	@docker run --detach -p 8000:$(host_port) $(app_name)

