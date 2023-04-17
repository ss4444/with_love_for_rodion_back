FROM python:3.8
WORKDIR /usr/app
#ENV PYTHONUNBUFFERED=1
RUN apt update && \
    apt-get -y install netcat
COPY  requirements.txt .
RUN pip3 install -r requirements.txt
RUN pip3 install decimer
#pip3 install install git+https://github.com/Kohulan/DECIMER-Image_Transformer.git
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
COPY .. /usr/app
CMD python3 main.py