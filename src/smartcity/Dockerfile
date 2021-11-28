# syntax=postgres/dockerfile:1
FROM python:3.9.9
ENV PYTHONUNBUFFERED=0
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN python  -m pdb manage.py collectstatic
CMD python manage.py runserver 0.0.0.0:8000
EXPOSE 8000