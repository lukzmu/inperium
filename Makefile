build:
	@docker compose build

run:
	@docker compose up

test:
	@docker compose run web test

lint:
	@docker compose run web lint

lint-autofix:
	@docker compose run web fmt

clean:
	@docker system prune -f --filter "label=eu.inperium=inperium"

update-lock:
	@docker compose run web poetry lock
