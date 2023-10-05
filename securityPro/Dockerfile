FROM python:3

WORKDIR .

RUN pip install django

COPY . .

EXPOSE 8000

CMD [ "python", "./manage.py", "runserver", "127.0.0.1:8000" ]