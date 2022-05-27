FROM python:3.8

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY src/requirements.txt .
RUN pip install -r requirements.txt
COPY src/. .

CMD [ "python", "app.py"]