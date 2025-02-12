FROM python:3.11.9

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .

CMD [ "./start_django.sh" ]