FROM python:3.11

RUN mkdir -p /opt/gu_ml
WORKDIR /opt/gu_ml

COPY . /opt/gu_ml
RUN pip install --upgrade pip
RUN pip install -r /opt/gu_ml/requirements.txt

EXPOSE 8001

CMD ["uvicorn", "gu_ml.main:app", "--host", "0.0.0.0", "--port", "80"]
