FROM python:3.9-slim

COPY ./src /app/src

COPY ./requirements.txt /app

WORKDIR /app

RUN set -eux \
    libressl-dev libffi-dev gcc musl-dev python3-dev \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r requirements.txt \
    && rm -rf /root/.cache/pip

# RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn","src.main:app","--host=0.0.0.0","--reload"]