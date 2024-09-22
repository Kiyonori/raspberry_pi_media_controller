FROM python:3.11.2

ARG APP_USER_ID
ARG APP_USER_NAME

RUN adduser ${APP_USER_NAME} --disabled-password --uid ${APP_USER_ID} --gecos "" --shell /sbin/nologin \
 && pip install pipenv

WORKDIR /home/${APP_USER_NAME}/raspberry-pi-media-controller
USER ${APP_USER_NAME}
ENTRYPOINT sleep infinity