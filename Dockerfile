FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir pandas matplotlib
COPY ledger.csv .
COPY plot_ledger.py .
CMD ["python", "plot_ledger.py"]
