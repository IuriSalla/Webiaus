FROM python:3.8
ENV PYTHONUNBUFFERED=1
RUN mkdir /Webiaus
WORKDIR /Webiaus
COPY django.txt /Webiaus/
RUN pip install -r django.txt
COPY . /Webiaus/
RUN echo 'import nltk' | python -m nltk.downloader all 
SHELL ["/bin/bash", "-c"]

