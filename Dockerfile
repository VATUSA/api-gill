FROM python:3.10-slim

EXPOSE 8000
WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . ./

CMD ["uvicorn", "app.v3.main:api", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000", "--reload"]
