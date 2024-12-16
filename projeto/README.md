 # Contact Management Application

## Overview

This project is a simple Contact Management web application that allows users to view, add, update, and delete contacts. It consists of a frontend served by Nginx and a backend API built with Flask. The application is containerized using Docker Compose, enabling easy deployment and scalability.

## Table of Contents

- Features
- Prerequisites
- Installation
- Usage
- Project Structure
- API Endpoints
- SSL Configuration
- Scaling
- Troubleshooting
- License

## Features

- **View Contacts:** Display a list of all contacts.
- **Add Contact:** Add a new contact with a name and phone number.
- **Update Contact:** Modify existing contact information.
- **Delete Contact:** Remove a contact from the list.
- **Secure Communication:** Uses SSL for secure communication between the frontend and backend.
- **Scalable Backend:** Backend service can be scaled to handle increased load.

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your machine.
- [Docker Compose](https://docs.docker.com/compose/install/) installed.
- Basic knowledge of Docker and Docker Compose.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/LuisBBandeira/networking-syllabus
    cd projeto
    ```

2. **Generate SSL Certificates:**

    Navigate to the `nginx/ssl` directory and run the SSL script.

    ```bash
    cd nginx/ssl
    ./ssl.sh
    cd ../..
    ```

    This script generates 

server.key

 and 

server.crt

 files required for SSL.

3. **Build and Run Containers:**

    Use Docker Compose to build and start the containers.

    ```bash
    docker-compose up --build
    ```

    - `--build`: Rebuild images if the Dockerfile has changed.

4. **Verify Services:**

    Check if the containers are running.

    ```bash
    docker-compose ps
    ```

## Usage

1. **Access the Application:**

    Open your browser and navigate to [https://localhost/](https://localhost/). You may need to bypass SSL warnings if using self-signed certificates.

2. **Manage Contacts:**

    - **View Contacts:** The homepage displays the list of existing contacts.
    - **Add Contact:** Use the form to add a new contact by entering a name and phone number.
    - **Update Contact:** Currently supported via the frontend interface.
    - **Delete Contact:** Click the "Delete" button next to a contact to remove it.

## Project Structure

```plaintext
.
├── backend
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── nginx
│   ├── nginx.conf
│   ├── ssl
│   │   ├── server.crt
│   │   ├── server.key
│   │   └── ssl.sh
├── docker-compose.yml
└── README.md
```

- **backend:** Contains the Flask application and related files.
- **nginx:** Contains the Nginx configuration and SSL certificates.
- **docker-compose.yml:** Defines the Docker Compose services.

## API Endpoints

The backend API provides the following endpoints:

- **GET `/contacts`**
  - **Description:** Retrieve all contacts.
  - **Response:** JSON array of contacts.
  
- **POST `/contacts`**
  - **Description:** Create a new contact.
  - **Request Body:**
    ```json
    {
      "name": "John Doe",
      "number": "+35199999999"
    }
    ```
  - **Response:** JSON object of the created contact.
  
- **PUT `/contacts/<id>`**
  - **Description:** Update an existing contact.
  - **Request Body:**
    ```json
    {
      "name": "Jane Doe",
      "number": "+35188888888"
    }
    ```
  - **Response:** JSON object of the updated contact.
  
- **DELETE `/contacts/<id>`**
  - **Description:** Delete a contact.
  - **Response:** `204 No Content` on successful deletion.

## SSL Configuration

SSL is configured using self-signed certificates for secure communication.

1. **Generate SSL Certificates:**

    The 

ssl.sh

 script in the `nginx/ssl` directory generates the necessary SSL certificates.

    ```bash
    cd nginx/ssl
    ./ssl.sh
    ```

2. **Nginx Configuration:**

    The 

nginx.conf

 file is set up to use the generated SSL certificates.

    ```nginx
    ssl_certificate /etc/nginx/ssl/server.crt;
    ssl_certificate_key /etc/nginx/ssl/server.key;
    ```

3. **Accessing the Application:**

    When accessing [https://localhost/](https://localhost/), your browser may warn about the self-signed certificate. You can proceed by adding an exception.

## Scaling

The backend service is configured to run multiple instances for better performance and reliability.

- **Docker Compose Configuration:**

    ```yaml
    backend:
      build: ./backend
      expose:
        - "5000"
      networks:
        - back_net
      deploy:
        replicas: 3
    ```

    - **replicas:** Number of backend instances.

- **Nginx Load Balancing:**

    Nginx is configured to load balance requests across the backend instances.

    ```nginx
    upstream backend_pool {
        server backend:5000;
    }
    ```

- **Scaling Up/Down:**

    To scale the backend service, use:

    ```bash
    docker-compose up -d --scale backend=5
    ```

    This command scales the backend service to 5 instances.

## Troubleshooting

- **Nginx 405 Method Not Allowed:**

    Ensure that Nginx is correctly proxying the HTTP methods. Verify the 

nginx.conf

 to allow `PUT` and `DELETE` methods.

- **SSL Certificate Issues:**

    If encountering SSL certificate errors, ensure that the certificates are correctly generated and paths are correctly specified in 

nginx.conf

.

    ```bash
    docker logs nginx_lb
    ```

- **Container Issues:**

    Check the status of containers and logs for any errors.

    ```bash
    docker-compose ps
    docker logs <container_name>
    ```

- **Port Conflicts:**

    Ensure that port `443` is not being used by another service.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

**Note:** This application uses in-memory storage for contacts. For production use, consider integrating a persistent database.

