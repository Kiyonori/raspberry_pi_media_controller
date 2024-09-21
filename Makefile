up:
	# .env が存在しない場合は .env.example をコピーする
	if [ ! -e .env ]; then \
		cp .env.example .env; \
		echo ".env を作成しました。"; \
	fi

	docker-compose build \
	&& docker-compose up -d

	# app/.env が存在しない場合は app/.env.example をコピーする
	if [ ! -e app/.env ]; then \
		cp app/.env.example app/.env; \
		echo "app/.env を作成しました。"; \
	fi

purge:
	docker-compose down
	docker image rm raspberry-pi-media-controller-python:latest