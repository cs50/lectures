FROM cs50/cli
EXPOSE 8080

ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y php5-sqlite sqlite3

RUN pip3 install Flask Flask-Session passlib SQLAlchemy

ENV FLASK_APP application.py
ENV FLASK_DEBUG 1

COPY . /srv/www
WORKDIR /srv/www

CMD flask run --host=0.0.0.0 --port=8080
