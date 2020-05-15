FROM python:latest
ADD . /assignment_flaskapp
WORKDIR /assignment_flaskapp
RUN pip install -r requirements.txt
COPY data.csv /assignment_flaskapp
CMD mongoimport --host mongodb -d mydb -c books --file /assignment_flaskapp/data.csv --headerline
