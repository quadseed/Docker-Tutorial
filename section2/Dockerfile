FROM python:3.9.12-slim-bullseye

RUN pip install --upgrade pip
RUN pip install sympy

COPY . .

CMD [ "python", "main.py" ]