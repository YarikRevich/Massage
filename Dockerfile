FROM python:3

COPY . /
RUN python3 -m pip install --upgrade pip && pip3 install -r requirements.txt
RUN python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver
