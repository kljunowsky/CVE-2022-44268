FROM python:3.10.6-alpine

RUN apk add --no-cache git gcc musl-dev
RUN git clone https://github.com/kljunowsky/CVE-2022-44268

WORKDIR /CVE-2022-44268

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "CVE-2022-44268.py"]
