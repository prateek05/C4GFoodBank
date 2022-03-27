FROM python:3.8.3-alpine
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev zlib-dev jpeg-dev file-dev
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .

COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
EXPOSE 8000