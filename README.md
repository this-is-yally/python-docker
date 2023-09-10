The .dockerignore file tells Docker to ignore some files and folders that are not needed for the image, such as .git and pycache.
The Dockerfile specifies the base image, the working directory, the dependencies, and the command to run the app. It also exposes port 8000 for the web app.
The app.py file imports the packages, loads the JSON file, defines a route for the web app, and returns a random quote from the JSON file as a response. It also logs the request and response to a file called app.log.
The compose.yaml file defines a service called web that uses the Dockerfile to build and run the app. It also mounts the current directory as a volume and maps port 8000 to port 80 on the host machine.
The requirements.txt file lists the Python packages that are needed for the app, such as Flask and requests.
The test.sh file is a shell script that runs some tests on the app using curl. It checks if the app is running, if it returns a valid JSON response, and if it logs the request and response correctly.


![image](https://github.com/this-is-yally/python-docker/assets/79525614/3119e23e-67f9-4f0b-b333-d57c59415311)
