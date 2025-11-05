# CTF Ghost Login Challenge

A Capture The Flag (CTF) web application challenge featuring a login bypass vulnerability.

## Overview

This is a Flask-based web application that simulates a "Starcloud Maintenance Console" with a login form. The challenge involves finding the correct credentials or exploiting vulnerabilities to access the admin panel and retrieve the flag.

## Challenge Description

Players must gain access to the admin panel to retrieve the flag. The application presents a login form that requires username and password authentication.

## Setup and Installation

### Prerequisites
- Docker
- Docker Compose

### Running the Application

1. Clone this repository:
```bash
git clone https://github.com/pking74/ctf-ghost-login.git
cd ctf-ghost-login
```

2. Build and run the application using Docker Compose:
```bash
docker-compose up --build
```

3. Access the application at `http://localhost:5000`

### Manual Setup (Alternative)

If you prefer to run without Docker:

1. Install Python 3.9+
2. Install Flask:
```bash
pip install flask
```
3. Run the application:
```bash
python app.py
```

## Project Structure

```
ctf-ghost-login/
├── app.py              # Main Flask application
├── Dockerfile          # Docker container configuration
├── docker-compose.yml  # Docker Compose setup
└── README.md           # This file
```

## Application Features

- **Login Form**: Username and password authentication
- **Error Handling**: Displays appropriate error messages
- **Admin Panel**: Protected area containing the flag
- **Dockerized**: Easy deployment with Docker

## Security Note

This application is intentionally vulnerable and designed for educational purposes in a CTF environment. Do not use this code in production environments.

## Flag Location

The flag can be found by successfully accessing the admin panel at `/admin`.

## Contributing

This is a CTF challenge repository. If you find issues or want to suggest improvements, please open an issue or submit a pull request.

## License

This project is for educational purposes only.
