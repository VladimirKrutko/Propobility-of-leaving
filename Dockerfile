FROM python:3.7-buster

RUN mkdir -p /app
WORKDIR /app

COPY main.py /app
COPY requirements.txt /app
COPY model.pickl /app

RUN pip install -U scikit-learn
RUN pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:app", "--port", "8000"]