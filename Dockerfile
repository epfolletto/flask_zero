FROM python:3.12.4-slim

WORKDIR app/

COPY . .

RUN pip install --no-cache-dir poetry

RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

COPY . /flask_zero/

ENV FLASK_APP=flask_zero.app

EXPOSE 5000

CMD poetry run flask run --host=0.0.0.0 --port=5000

