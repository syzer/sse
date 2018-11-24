# sse

Semantic Search Engine

## Idea

A biomedical semantic search engine using omop vocabularies.
The goal is to allow to search for specific entities in text.

![alt text](https://travis-ci.org/escodebar/sse.svg?branch_master)

## Setup Development

### API

To setup the API, create a Python virtual environment and install the backend.

```shell
$ git clone git@github.com/escodebar/sse.git && cd sse
$ python3 -m venv . && source bin/activate
$ (sse) python3 -m pip install -e . -r requirements.txt -c constraints.txt
$ (sse) python3 manage.py migrate
```

Then run the server with:
```shell
$ (sse) python3 manage.py runserver
```
