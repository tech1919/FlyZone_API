FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

ENV PORT 80
EXPOSE 80

RUN uvicorn main:app --host 0.0.0.0 --port 80
