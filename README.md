# Weather Data Pipeline 

## Overview

This project implements an **ETL (Extract–Transform–Load) data pipeline** that retrieves real-time weather data from an external API, processes it, and stores the results in a local **SQLite** database.

---

## Architecture

The pipeline follows a standard ETL workflow:

```
Extract → Transform → Load
```

### Components

* **Extract** – Fetches weather data from a public weather API
* **Transform** – Cleans and structures the raw API response
* **Load** – Stores processed data in an SQLite database
* **Logging** – Tracks pipeline execution and errors

---

## Repository Setup

### 1. Clone the repository

```bash
git clone https://github.com/Maggarb/Daily-Weather-Data-Pipeline
cd weather-pipeline
```

---

### 2. Install dependencies

It is recommended to use a virtual environment.

```bash
pip install -r requirements.txt
```

---

### 3. Configure environment variables

Create a `.env` file in the project root:

```
LATITUDE=64.1466
LONGITUDE=-21.9426
```

---

## Running the Pipeline

Execute the pipeline:

```bash
python run_pipeline.py
```

The pipeline will:

1. Fetch current weather data
2. Transform the API response
3. Store results in `data/weather.db`

---

## Checking Stored Data

To view stored weather records:

```bash
python check_db.py
```

This prints all records currently saved in the database.

---

## Logging

Pipeline execution logs include:

* pipeline start and completion
* successful data loading
* error handling and failures

Logging helps monitor pipeline reliability and simplifies debugging.

---

## Technologies Used

* Python
* SQLite
* python-dotenv
* REST API integration
* Standard Python logging module

---

