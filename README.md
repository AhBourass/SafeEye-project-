# SafeEye Project

SafeEye is a unified cybersecurity solution designed to protect non-technical users from network threats and phishing attacks. Even on public networks, SafeEye helps you identify devices and stay safe.

## 🚀 Getting Started

Follow these steps to set up the project on your local machine.

### Prerequisites
*   **Docker Desktop** (Make sure it's running)
*   **Git**

### 1. Clone the Repository
```bash
git clone <repository-url>
cd SafeEye-project-
```

### 2. Configure Environment
Copy the example environment file to create your local configuration:
```bash
cp .env.example .env
# OR on Windows Command Prompt:
# copy .env.example .env
```

### 3. Run the Application
Start the entire stack (Backend, Database, and Agent) with Docker Compose:
```bash
docker compose up --build -d
```

### 4. Verify Installation
*   **Backend API**: Open [http://localhost:8000](http://localhost:8000). You should see:
    > `{"status":"online","message":"SafeEye Backend is running"}`
*   **API Documentation**: Open [http://localhost:8000/docs](http://localhost:8000/docs) to see the Swagger UI.

### 5. Access the Database
You can connect to the PostgreSQL database using any client (pgAdmin, DBeaver, DataGrip).

*   **Host**: `localhost`
*   **Port**: `5433` *(Note: It's mapped to 5433 externally to avoid conflicts with local Postgres)*
*   **Database**: `SafeEye`
*   **Username**: `admin`
*   **Password**: `securepass123`

## 🛠 Project Structure
*   `agent/`: Python-based network scanner (runs as a separate container).
*   `backend/`: FastAPI application handling API requests and database logic.
*   `database/`: SQL scripts for initialization (`init.sql`).
*   `docker-compose.yml`: Orchestrates the services.

## 🔴 Troubleshooting
*   **Port Conflicts**: If port `5433` is taken, edit `docker-compose.yml` and change `"5433:5432"` to a different port like `"5434:5432"`.
*   **Database Connection Errors**: Ensure the container is running with `docker compose ps`. If the database isn't ready, wait a few seconds and try again.
