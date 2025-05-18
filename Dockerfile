# Dockerfile

FROM python:3.11-slim

# Set working directory to /app
WORKDIR /app

# Copy contents of ./app into /app
COPY app/ .

# Install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose and run
ENV PORT=8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
