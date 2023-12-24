FROM python:3.10-alpine3.17

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

COPY .. /code

#CMD ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "5000"]
CMD ["python", "main.py"]