.PHONY: default
default: run

.PHONY: build
build:
	docker build -t src10 .

.PHONY: rebuild
rebuild:
	docker build --no-cache -t src10 .

.PHONY: run
run:
	docker run -i --name src10 --rm -p 8080:8080 -p 8081:8081 -v "$(PWD)":/srv/www -t src10

.PHONY: shell
shell:
	docker run -i --name src10 --rm -p 8080:8080 -p 8081:8081 -v "$(PWD)":/srv/www -t src10 bash -l
