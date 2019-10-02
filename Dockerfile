FROM python:3-alpine

MAINTAINER Jake Pifer

COPY __init__ /flaskr

WORKDIR /flaskr

RUN pip install -r requirements.txt

CMD ["python", "__init__.py"]