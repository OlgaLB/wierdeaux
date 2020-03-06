FROM python:3.6-slim

RUN apt-get update -y \
  && apt-get install -y wget \
  && apt-get install bzip2 \
  && apt install -y libgtk-3-0 libx11-xcb1 libdbus-1-dev libdbus-glib-1-2 libxt6

RUN mkdir work
WORKDIR /work

RUN chmod 777 /work
COPY HoeWarmIsHetInDelft.py /work

RUN cd /work

RUN pip3 install --upgrade pip
RUN pip3 install requests

RUN wget https://ftp.mozilla.org/pub/firefox/releases/72.0/linux-x86_64/en-US/firefox-72.0.tar.bz2
RUN tar -xvf firefox-72.0.tar.bz2
RUN mv firefox /opt/firefox72
RUN ln -s /opt/firefox72/firefox /usr/bin/firefox
RUN ls /opt/firefox72
RUN firefox --version

RUN pip install beautifulsoup4
RUN pip install selenium
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
RUN tar -xvzf geckodriver-v0.26.0-linux64.tar.gz
RUN chmod +x geckodriver

ENV PATH=/work:$PATH

CMD python3 HoeWarmIsHetInDelft.py
