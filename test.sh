#!/bin/bash

# Build the Docker image
docker build -t flask-example .

# Run a container from the built image
docker run -d -p 5000:5000 --name flask-app flask-example

# Wait for the Flask app to start
sleep 5

# Send a request to the app and store the response
response=$(curl -s http://localhost:5000)

# Check if the response contains the expected message
if [[ $response == *"Hello, my dear viewer/recruiter! It is just an example on Flask for Docker"* ]]; then
  echo "Dockerfile test passed: Expected message found."
  exit 0
else
  echo "Dockerfile test failed: Expected message not found."
  exit 1
fi

# Cleanup - stop and remove the test container
docker stop flask-app
docker rm flask-app
