FROM python:3.10-slim

# Create the working directory
RUN mkdir -p /src

# Directorio de trabajo
WORKDIR /src

# Copia archivos de dependencias para aprovechar caché
COPY pyproject.toml poetry.lock* ./

# Instala Poetry con pip
RUN pip install --no-cache-dir poetry

# Configura Poetry para no crear entornos virtuales
RUN poetry config virtualenvs.create false

# Instala las dependencias del proyecto
RUN poetry install --no-root --no-interaction --no-ansi

# Expose the port for Jupyter Notebook
EXPOSE 8888

# Run Jupyter Notebook with necessary options
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root",  "--NotebookApp.token=''", "--NotebookApp.password=''"]
