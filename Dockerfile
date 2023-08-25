FROM python:3.7-alpine
WORKDIR /home
ENV FLASK_APP=meu_site.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]