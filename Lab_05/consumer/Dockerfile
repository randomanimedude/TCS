FROM python:3.9
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY consumer.py consumer.py
CMD ["python", "consumer.py"]
