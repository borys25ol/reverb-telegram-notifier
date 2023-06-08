Reverb Telegram Notifier
====================

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Pre-commit: enabled](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat)](https://github.com/pre-commit/pre-commit)

## Description

This project can be used to receive notifications in Telegram when a new product will be listed for some category (https://reverb.com)

Developing
-----------

Install pre-commit hooks to ensure code quality checks and style checks

    $ make install_hooks

Then see `Configuration` section

You can also use these commands during dev process:

- To run mypy checks

      $ make types

- To run flake8 checks

      $ make style

- To run black checks:

      $ make format

- To run together:

      $ make lint


Configuration
--------------

Replace `.env.example` with real `.env`, changing placeholders

```
TELEGRAM_BOT_TOKEN=<token>
TELEGRAM_CHAT_ID=<public/group-id>
MONGO_URI=<mongo-uri>
MONGO_DB=<mongo-collection>
MONGO_PRODUCT_COLLECTION=<mongo-collection>
MONGO_SCRAPING_LINKS_COLLECTION=<mongo-collection>
```


Local install
-------------

Setup and activate a python3 virtualenv via your preferred method. e.g. and install production requirements:


    $ make ve

For remove virtualenv:


    $ make clean


Local run
-------------
Run spider locally:

    $  scrapy crawl reverb.com

Run docker containers:

    $  make docker_up
