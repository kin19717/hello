FROM python:3.6
COPY . /app
EXPOSE 8080
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "hello.py", "python -m flask run"]
