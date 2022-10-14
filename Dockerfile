FROM python:3.8.14-slim 


WORKDIR /main_app

COPY requirements.txt .

RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

ADD app/ .

CMD ["python", "app.py"]