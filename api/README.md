# FastAPI Example Project

A simple FastAPI project with a hello world endpoint and OpenAPI specification.

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

To run the application, execute:
```bash
python main.py
```

The server will start on `http://localhost:8000`

## Available Endpoints

- `GET /`: Hello World endpoint
- `GET /openapi-json`: OpenAPI specification in JSON format
- `GET /docs`: Interactive API documentation (Swagger UI)
