# Containerized Flask App

Flask app containerized with Docker + Compose, PostgreSQL backend.

## Stack
- **Flask** — Python web framework
- **PostgreSQL** — relational database
- **Docker** — containerization
- **Docker Compose** — multi-container orchestration

## Project Structure
```
flask-app/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile          # Container blueprint
└── docker-compose.yml  # Runs Flask + PostgreSQL together
```

## Usage

**Start the app:**
```bash
docker-compose up --build
```

**Test it:**
- http://localhost:5000 — Hello message
- http://localhost:5000/db — Database connection test

**Stop the app:**
```bash
docker-compose down
```

## Tech
`Docker` `Python` `Flask` `PostgreSQL`
