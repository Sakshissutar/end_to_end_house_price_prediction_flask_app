FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["python", "app.py", "--server.port=5000", "--server.address=0.0.0.0"]