# Desparchado

[![Join the chat at https://gitter.im/vero4karu/desparchado](https://badges.gitter.im/vero4karu/desparchado.svg)](https://gitter.im/vero4karu/desparchado?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![Coverage Status](https://coveralls.io/repos/vero4karu/desparchado/badge.svg?branch=master&service=github)](https://coveralls.io/github/vero4karu/desparchado?branch=master)
[![Build Status](https://travis-ci.org/vero4karu/desparchado.svg?branch=master)](https://travis-ci.org/vero4karu/desparchado)

# Installation

    $ createdb desparchado
    $ psql desparchado
    desparchado=# CREATE EXTENSION postgis;

    $ mkvirtualenv desparchado -p python3

    $ pip install uwsgi

    $ pip install -r requirements.txt
    $ ./manage.py migrate
    $ ./manage.py collectstatic --no-input
    $ django-admin compilemessages

