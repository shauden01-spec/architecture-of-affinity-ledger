# Use a lightweight, secure Python base image
FROM python:3.11-slim

# Establish secure operational working directory
WORKDIR /app

# Install standard analytical packages natively
RUN pip install --no-cache-dir pandas matplotlib

# Copy tracking datasets and processing code into container layers
COPY ledger.csv .
COPY plot_ledger.py .

# Execute the optical spectrum plotter as the primary container layer command
CMD ["python", "plot_ledger.py"]
