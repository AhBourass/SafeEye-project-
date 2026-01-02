# Backend Dockerfile - Cybersécurité Accessible
# Multi-stage build for optimized production image

# ============================================
# Stage 1: Base Python Image
# ============================================
FROM python:3.11-slim AS base

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Create app user (security best practice)
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set working directory
WORKDIR /app

# ============================================
# Stage 2: Dependencies
# ============================================
FROM base AS dependencies

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (Docker layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ============================================
# Stage 3: Runtime
# ============================================
FROM base AS runtime

# Install only runtime dependencies (smaller image)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy Python packages from dependencies stage
COPY --from=dependencies /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=dependencies /usr/local/bin /usr/local/bin

# Copy application code
COPY --chown=appuser:appuser . /app

# Create necessary directories
RUN mkdir -p /app/logs /app/certs && \
    chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Default command (can be overridden in docker-compose)
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]

# ============================================
# Build Instructions:
# ============================================
# Development:
#   docker build -t cyber-backend:dev .
#   docker run -p 8000:8000 cyber-backend:dev
#
# Production:
#   docker build -t cyber-backend:latest .
#   docker run -d -p 8000:8000 --name backend cyber-backend:latest
#
# With docker-compose (recommended):
#   docker-compose build backend
#   docker-compose up backend
#
# Image size: ~200MB (optimized with multi-stage build)
