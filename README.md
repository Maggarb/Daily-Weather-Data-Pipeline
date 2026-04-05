Weather Data Pipeline 

This project implements an ETL (Extract–Transform–Load) data pipeline that retrieves real-time weather data from an external API, processes it, and stores it in a local SQLite database.

The pipeline demonstrates core data engineering concepts, including modular architecture, environment configuration, logging, and persistent data storage.

Architecture

The pipeline follows a standard ETL workflow:

Extract → Transform → Load
Components
Extract – Fetches weather data from a public weather API.
Transform – Cleans and structures the raw API response.
Load – Stores processed data into an SQLite database.
Logging – Tracks pipeline execution and errors.

Running the Pipeline

Execute: python -m pipeline.run_pipeline

The pipeline will:

Fetch current weather data
Transform the response
Store results in data/weather.db

Checking Stored Data, Run: python check_db.py

This prints all stored weather records.

Logging

Pipeline execution logs include:

pipeline start/end
successful data loads
error handling

Logs help monitor pipeline reliability and debugging.
