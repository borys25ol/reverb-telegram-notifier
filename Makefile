ve:
	python3 -m venv .ve; \
	. .ve/bin/activate; \
	pip install -r requirements.txt; \

docker_build:
	docker-compose up -d --build

docker_up:
	docker-compose up -d

docker_start:
	docker-compose start

docker_down:
	docker-compose down

docker_destroy:
	docker-compose down -v

docker_stop:
	docker-compose stop

docker_restart:
	docker-compose stop
	docker-compose up -d

docker_logs:
	docker-compose logs --tail=100 -f

install_hooks:
	pip install -r requirements-ci.txt; \
	pre-commit install; \

run_hooks:
	pre-commit run --all-files

check_style:
	flake8 crawl && isort crawl --diff && black crawl --check

lint:
	flake8 crawl && isort crawl && black crawl

types:
	mypy --namespace-packages -p "crawl" --config-file setup.cfg