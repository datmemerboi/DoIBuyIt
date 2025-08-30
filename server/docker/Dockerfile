# Use Python 3.13 image to match your project
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install uv for faster Python package management
RUN pip install uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install Python dependencies
RUN uv sync --frozen

# Copy project files
COPY . .

# Expose the port Django runs on
EXPOSE 8000
