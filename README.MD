# Flask CRUD API with Docker

This repository contains a simple Flask CRUD (Create, Read, Update, Delete) API for managing products, along with Docker configuration for containerization.

## Flask API

### Project Structure

The Flask API consists of the following files:

- `app.py`: Main file containing the Flask application and SQLAlchemy configuration.
- `Dockerfile`: Configuration file for building a Docker image.
- `requirements.txt`: List of Python dependencies.

### Usage

1. **Run Locally:**

    ```bash
    # Install dependencies
    pip install -r requirements.txt

    # Run Flask application
    python app.py
    ```

    The API will be accessible at `http://localhost:5000`.

2. **Docker:**

    Build the Docker image and run the container:

    ```bash
    # Build Docker image
    docker build -t flask-crud-api .

    # Run Docker container
    docker run -p 5000:5000 flask-crud-api
    ```

    The API will be accessible at `http://localhost:5000`.

### API Endpoints

- **GET /productos:** Get all products.
- **GET /productos/{id}:** Get a product by ID.
- **POST /productos:** Create a new product.
- **PUT /productos/{id}:** Update a product by ID.
- **DELETE /productos/{id}:** Delete a product by ID.

## Docker Configuration

The Dockerfile provided is configured to run the Flask application in a Docker container. Follow these steps to build and run the Docker container:

1. **Build Docker Image:**

    ```bash
    docker build -t flask-crud-api .
    ```

2. **Run Docker Container:**

    ```bash
    docker run -p 5000:5000 flask-crud-api
    ```

    The Flask API will be accessible at `http://localhost:5000` from your local machine.

Feel free to explore, customize, and extend this Flask CRUD API for your projects. If you encounter any issues or have questions, please refer to the Flask and Docker documentation for further assistance.