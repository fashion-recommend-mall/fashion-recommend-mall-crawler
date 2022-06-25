FROM python:3.10.0

WORKDIR /usr/local
RUN apt-get -y update
RUN apt install wget
RUN apt install unzip  
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt -y install ./google-chrome-stable_current_amd64.deb
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/` curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin

RUN apt-get install openjdk-11-jdk -y

COPY ./ /home/crwaler/
WORKDIR /home/crwaler/
RUN pip3 install celery
RUN pip3 install -r requirements.txt

CMD python3 -m celery -A src.celery_setting worker -l INFO
