FROM python:3.10

WORKDIR otus

COPY requirements .

RUN pip install -U pip
RUN pip install -r requirements

COPY . .

CMD ["pytest", "--browser", "chrome"]