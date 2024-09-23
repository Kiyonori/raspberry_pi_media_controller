up:
	# containers/.env が存在しない場合は containers/.env.example をコピーする
	if [ ! -e containers/.env ]; then \
		cp containers/.env.example containers/.env; \
		echo "containers/.env を作成しました。"; \
	fi

	# raspberry-pi-media-controller/.env が存在しない場合は raspberry-pi-media-controller/.env.example をコピーする
	if [ ! -e raspberry-pi-media-controller/.env ]; then \
		cp raspberry-pi-media-controller/.env.example raspberry-pi-media-controller/.env; \
		echo "raspberry-pi-media-controller/.env を作成しました。"; \
	fi

	cd containers \
	&& docker-compose build \
	&& docker-compose up -d
purge:
	cd containers \
	&& docker-compose down \
	&& docker image rm raspberry-pi-media-controller-python:latest