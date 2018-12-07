FROM python:3.4-alpine
COPY requirements.txt /
RUN pip install -r requirements.txt

ADD . /root
WORKDIR /root
ENV PYTHONPATH /root

EXPOSE 5000

CMD python3 /root/src/run.py