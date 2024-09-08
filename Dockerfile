FROM python:3.12


RUN apt-get update && apt-get install -y firefox-esr xvfb

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]

