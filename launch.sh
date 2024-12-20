#!/bin/bash

# Script to launch a docker-compose.yaml stack

COMPOSE_FILE="docker-compose.yaml" # Set the name of your docker-compose file

# Check if the docker-compose file exists
if [[ ! -f $COMPOSE_FILE ]]; then
    echo "Error: $COMPOSE_FILE not found in the current directory."
    exit 1
fi

# Function to clean up Docker stack on exit
cleanup() {
    echo -e "\nStopping and removing Docker containers..."
    docker compose down
    echo "Clean-up complete."
    exit 0
}

# Trap SIGINT (Ctrl+C) and SIGTERM to trigger clean-up
trap cleanup SIGINT SIGTERM

# Build and start the Docker Compose stack
echo "Starting Docker Compose stack..."
docker compose up --build -d

# Tail logs
echo "Tailing logs (Press Ctrl+C to stop and clean up)..."
docker compose logs -f
