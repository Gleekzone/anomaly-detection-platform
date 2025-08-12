FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock* ./

# Install Poetry using pip
RUN pip install --no-cache-dir poetry

# Configure Poetry to not create virtual environments
RUN poetry config virtualenvs.create false

# Install project dependencies without installing the root package
RUN poetry install --no-root --no-interaction --no-ansi

# Copy the rest of the application code
COPY ./app ./app

# Expose port 8000
EXPOSE 8000

# Command to run the app with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]