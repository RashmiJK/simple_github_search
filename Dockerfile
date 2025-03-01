FROM python:3.12

WORKDIR /code

# Copy the necessary files
COPY pyproject.toml .
COPY src/ src/

# Install dependencies in editable mode
RUN python -m pip install --upgrade pip
RUN python -m pip install -e .

EXPOSE 8000

# Set the default command to run the application
CMD ["python", "-m", "fastapi", "run", "src/app.py", "--host", "0.0.0.0", "--port", "8000"]
