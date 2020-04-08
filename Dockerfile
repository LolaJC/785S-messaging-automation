FROM joyzoursky/python-chromedriver:3.8-selenium
LABEL maintainer="lola@jeancadene.net"
RUN mkdir /messaging
WORKDIR /messaging
COPY ./requirements.txt /messaging/.
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY *.py /messaging/
EXPOSE 3000
CMD gunicorn --bind 0.0.0.0:3000 wsgi:app
