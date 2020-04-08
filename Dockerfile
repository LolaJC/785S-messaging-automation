FROM joyzoursky/python-chromedriver:3.8-selenium
RUN mkdir /messaging
WORKDIR /messaging
COPY ./requirements.txt /messaging/.
RUN cd /messaging && pip install --upgrade pip && pip install -r requirements.txt
COPY . /messaging/.
EXPOSE 3000
CMD gunicorn --bind 0.0.0.0:3000 wsgi:app
