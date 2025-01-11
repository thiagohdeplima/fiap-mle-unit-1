FROM python:3-alpine3.21

WORKDIR /srv/app

COPY . .

RUN pip install -r requirements.txt

USER nobody

CMD ["python", "app.py"]
