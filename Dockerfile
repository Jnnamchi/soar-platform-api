FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN groupadd -r app && useradd -r -g app -d /app -s /sbin/nologin -c "Image user" app
RUN curl -sSL https://install.python-poetry.org | python3 -

RUN /root/.local/bin/poetry config virtualenvs.create false

RUN mkdir /app
ADD poetry.lock /app
ADD pyproject.toml /app
WORKDIR app
RUN /root/.local/bin/poetry install

COPY src /app
RUN chown -R app:app /app
USER app
EXPOSE 5000
CMD ["uwsgi", "--http", "0.0.0.0:5000", "--master", "-p 4", "-w", "app:app"]