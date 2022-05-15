FROM python:3.9.12-slim-bullseye

RUN pip install --upgrade pip
RUN pip install sympy

RUN mkdir -p /project/src

WORKDIR /project/src

CMD [ "python", "main.py" ]