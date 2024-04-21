# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy the current directory contents into the container at /app
COPY . /app

# Disable Poetry's virtual environment as the container itself provides isolation
RUN poetry config virtualenvs.create false

# Install project dependencies
RUN poetry install --no-interaction --no-ansi --no-dev

# Make port 80 available to the world outside this container

ARG DEFAULT_KEY=1234
ARG DEFAULT_NAME=DEFAULT_GPT
ARG DEF_PORT

ENV KEY $DEFAULT_KEY
ENV NAME $DEFAULT_NAME
ENV PORT $DEF_PORT


EXPOSE $PORT

# Run the app when the container launches
CMD ["poetry", "run", "python", "src/main.py"]

