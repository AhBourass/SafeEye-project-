# Agent Dockerfile - Cybersécurité Accessible
# For testing purposes - in production, agent runs on user's host machine

FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

# Install system dependencies for network scanning
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpcap-dev \
    tcpdump \
    net-tools \
    iputils-ping \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . /app

# Create logs directory
RUN mkdir -p /app/logs

# Note: Agent requires elevated privileges for network scanning
# This is handled by docker-compose with cap_add: NET_ADMIN

# Default command (manual execution)
CMD ["python", "src/scanner.py"]

# ============================================
# Build Instructions:
# ============================================
# Build:
#   docker build -t cyber-agent:latest .
#
# Run (with network privileges):
#   docker run --cap-add=NET_ADMIN --net=host cyber-agent:latest
#
# With docker-compose (recommended):
#   docker-compose run agent
#
# IMPORTANT NOTES:
# ============================================
# 1. This Dockerfile is for TESTING ONLY
# 2. In production, users run the agent directly on their machine
# 3. Network scanning requires:
#    - --cap-add=NET_ADMIN (Docker capability)
#    - --net=host (access to host network)
#    - Root privileges (handled by Docker)
#
# 4. For real deployment, users will:
#    - Install Python 3.10+
#    - pip install -r requirements.txt
#    - sudo python src/scanner.py
#
# Image size: ~250MB (includes network tools)
