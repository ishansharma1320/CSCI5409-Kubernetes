FROM python:3.8-slim


WORKDIR /app

COPY . .

EXPOSE 7000 

RUN pip install -r requirements.txt
CMD ["python","app.py"]