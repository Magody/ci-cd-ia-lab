FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
COPY model/model.pkl /app/model/model.pkl

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app.app:app"]
