FROM python:3.8.14-slim 


WORKDIR /main_app

COPY requirements.txt .

RUN pip install -r requirements.txt --root-user-action=ignore

ADD app/ .

CMD ["python", "app.py"]