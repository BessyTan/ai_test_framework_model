FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["pytest", "tests/", "--html=reports/report.html", "--self-contained-html"]
