FROM python:3.12.11-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy all files from the current directory to the container's working directory
COPY . /usr/src/app

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Expose the port that Django will run on
EXPOSE 8000

# Set the Django secret key as an environment variable
ENV DJANGO_SECRET_KEY='django-insecure-a4eiw-80uw3nh*30ynmesl(cfeh)0fd4)n&(gojyg!yo9oly@d'

# Run the Django server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
