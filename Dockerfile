FROM python:3.8.2-slim-buster

ADD poxter/ /poxter/
WORKDIR /poxter/

RUN pip install --upgrade -r requirements.txt

CMD [ "python", "poxter.py" ]
