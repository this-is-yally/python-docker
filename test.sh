#!/bin/bash

# Build the Docker image
docker build -t flask-app .

# Run a container from the built image
docker run -d -p 8000:8000 --name flask-container flask-app

# Wait for the Flask app to start (you can add a more sophisticated check here)
sleep 5

# Send a request to the app and store the response
response=$(curl -s http://localhost:8000)

# Check if the response contains the expected message
if [[ $response == *"This is a more complex Flask example."* ]]; then
  echo "Dockerfile test passed: Expected message found."
  exit 0
else
  echo "Dockerfile test failed: Expected message not found."
  exit 1
fi

# Cleanup - stop and remove the test container
docker stop flask-container
docker rm flask-container
