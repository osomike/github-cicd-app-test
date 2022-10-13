FROM python:3.8.14-slim 


WORKDIR /main_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app/* .

CMD ["python", "main.py"]