.PHONY: run

PORT ?= 8080

run:
	@docker build -t unit-converter-backend .
	@docker run -p $(PORT):8080 unit-converter-backend
