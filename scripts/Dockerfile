FROM python:3.9-slim

WORKDIR /app

# Install Selenium
RUN pip install selenium

# Copy the script
COPY main.py .

CMD ["python", "main.py"]