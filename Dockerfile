FROM python:3.8.12

WORKDIR /usr/src/app

COPY . .

RUN apt update && \
    pip install poetry && \
    poetry install

CMD ["poetry", "run", "python3", "index.py"]