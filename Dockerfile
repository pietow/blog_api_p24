# Base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1


# Set work directory
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3-dev \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Run migrations
RUN python manage.py migrate

# Expose the port on which Django will run
EXPOSE 8000

# Command to run Gunicorn
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "django_project.wsgi:application"]

