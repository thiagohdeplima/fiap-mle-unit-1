FROM python:3-alpine3.21

ENV PORT 8080

WORKDIR /srv/app

COPY . .

RUN pip install -r requirements.txt

USER nobody

CMD ["sh", "-c", "python -m gunicorn -w 4 -b 0.0.0.0:${PORT} app:app"]
