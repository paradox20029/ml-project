FROM python:3.10-slim-buster
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

# Add this line to document the port
EXPOSE 5000
      
CMD ["python3", "application.py"]