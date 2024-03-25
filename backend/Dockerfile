FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=server.py

EXPOSE 3000
EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]