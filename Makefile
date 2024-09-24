up:
	# containers/.env が存在しない場合は containers/.env.example をコピーする
	if [ ! -e containers/.env ]; then \
		cp containers/.env.example containers/.env; \
		echo "containers/.env を作成しました。"; \
	fi

	# raspberry_pi_media_controller/.env が存在しない場合は raspberry_pi_media_controller/.env.example をコピーする
	if [ ! -e raspberry_pi_media_controller/.env ]; then \
		cp raspberry_pi_media_controller/.env.example raspberry_pi_media_controller/.env; \
		echo "raspberry_pi_media_controller/.env を作成しました。"; \
	fi

	cd containers \
	&& docker-compose build \
	&& docker-compose up -d \
	&& docker-compose exec python bash -c "pip install -r requirements.txt" \
	&& docker-compose exec python bash -c "pipenv install -d pytest"
purge:
	cd containers \
	&& docker-compose down \
	&& docker image rm raspberry-pi-media-controller-python:latest