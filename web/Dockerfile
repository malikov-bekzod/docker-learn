FROM python:3

WORKDIR /webapp

COPY . .

EXPOSE 8000

RUN pip install -r requirements.txt

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]