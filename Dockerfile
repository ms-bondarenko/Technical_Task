FROM python:3

WORKDIR /usr/local/app

COPY requirements.txt ./

COPY Pages ./Pages

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "test_Login_Page.py"]
