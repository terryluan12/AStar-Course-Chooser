FROM python:3.14.0-bookworm

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "wsgi:app", "--bind", "0.0.0.0:8000"]