FROM python:3.11.9-alpine3.19
LABEL maintainer="samuelzv@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./django/app /app
COPY ./django/requirements /app/requirements
COPY ./django/scripts /scripts
COPY ./svelte/dist /svelte/dist


WORKDIR /app
EXPOSE 8000 3000

# /py/bin/pip install -r /requirements/local.txt && \

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache rust cargo && \
    apk add --update --no-cache gettext-dev && \
    apk add --update --no-cache npm && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev linux-headers && \
    /py/bin/pip install -r requirements/local.txt && \
    apk del .tmp-deps && \
    npm install && \
    adduser --disabled-password --no-create-home app && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R app:app /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER app

CMD ["run.sh"]
