FROM python:3.8

WORKDIR /projet13

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3" , "manage.py", "runserver"]