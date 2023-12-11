# Dockerized Flask App

## Description
This is a simple Flask web application dockerized for easy deployment.

## Prerequisites
- Docker installed on your machine

## How to Run
1. Clone this repository.
2. Open a terminal in the project directory.
3. Build the Docker image: `docker build -t my-python-app .`
4. Run the Docker container: `docker run -p 4000:80 my-python-app`

The app will be accessible at [http://127.0.0.1:4000](http://127.0.0.1:4000).

## Important Note
This application is set up for development purposes. Do not use the built-in server in a production environment.

## Contributing
If you find issues or want to contribute, feel free to open a pull request or an issue.

## License
This project is licensed under the [MIT License](LICENSE).
