up:
	# .env が存在しない場合は .env.example をコピーする
	if [ ! -e .env ]; then \
		cp .env.example .env; \
		echo ".env を作成しました。"; \
	fi

	docker-compose build \
	&& docker-compose up -d

purge:
	docker-compose down
	docker image rm raspberry-pi-media-controller-python:latest