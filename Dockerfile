FROM python:3.9

WORKDIR /usr/src/api

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN mkdir /songs

COPY . .

CMD ["gunicorn", "--bind","0.0.0.0:5000","main:app"]