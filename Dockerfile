# Use official python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

# Streamlit config - run on 0.0.0.0:8501 to be accessible in container
EXPOSE 8501
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_ENABLE_CORS=false
ENV STREAMLIT_SERVER_PORT=8501

# DATABASE URL - defaults to SQLite, override with PostgreSQL URL at runtime
# PostgreSQL format: postgresql://username:password@host:port/database
ENV DATABASE_URL="sqlite:///./test.db"

# Command to run the app
CMD ["streamlit", "run", "app.py"]