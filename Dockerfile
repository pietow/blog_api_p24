FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
python3-dev \
build-essential \
libpq-dev \
&& rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip 
RUN pip install -r requirements.txt 

COPY . .

RUN python manage.py collectstatic --noinput

RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "django_project.wsgi:application"]





