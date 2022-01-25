FROM python:3.8

COPY rest_api ./rest_api

RUN pip install -r rest_api/requirements.txt

CMD ["python3", "rest_api/rest_api.py"]