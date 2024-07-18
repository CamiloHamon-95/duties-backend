FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /app

CMD [ "uvicorn", "main:app",  "--host", "0.0.0.0", "--port", "5000"]