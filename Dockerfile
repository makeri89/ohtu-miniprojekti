FROM ubuntu:20.04

WORKDIR /usr/src/app

COPY . .

RUN apt update && apt install -y curl python3 python3.8-venv python3-pip

RUN pip install poetry

RUN poetry install

# RUN poetry run python3 src/index.py &

# CMD ["poetry", "run", "python3", "src/index.py"]
CMD ["bash"]