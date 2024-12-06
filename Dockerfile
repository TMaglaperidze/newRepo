FROM python:3.12-slim

COPY app.py .

 # Install Flask

RUN pip install flask
EXPOSE 5000

CMD ["python", "app.py"]


# CMD ["sleep", "60"]
# ENTRYPOINT [./ngin]
