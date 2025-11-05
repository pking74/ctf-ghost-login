FROM python:3.9-slim

WORKDIR /app
COPY app.py .

RUN pip install flask

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run", "--port=5000"]