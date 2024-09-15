FROM python:3.11.2

ARG APP_USER_ID
ARG APP_USER_NAME

RUN adduser ${APP_USER_NAME} --disabled-password --uid ${APP_USER_ID} --gecos "" --shell /sbin/nologin
WORKDIR /home/${APP_USER_NAME}
USER ${APP_USER_NAME}
ENTRYPOINT sleep infinity