FROM python:3.8-slim


WORKDIR /app

COPY . .

EXPOSE 6000

RUN pip install -r requirements.txt
CMD ["python","app.py"]