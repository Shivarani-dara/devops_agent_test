FROM python:3.10

WORKDIR /app

COPY requirements_missing.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
