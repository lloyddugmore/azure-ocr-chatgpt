FROM python:3.11-slim

RUN python3 -m pip install --upgrade pip

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --no-cache-dir -r requirements.txt

COPY . ./code/

CMD ["python", "/code/attempt_2.py"]
