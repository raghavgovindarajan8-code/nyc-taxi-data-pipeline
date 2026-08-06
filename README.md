# NYC Taxi Data Pipeline

Production-style Data Engineering Pipeline built using Python and SQL.

## Pipeline Workflow

1. Load NYC Taxi trip dataset
2. Perform Data Quality Checks (DDQ)
3. Clean and validate data
4. Transform data
5. Save cleaned dataset
6. Generate pipeline logs

---

## Data Quality Checks (DDQ)

Before any transformations, the pipeline performs automated Data Quality Checks (DDQs).

### Checks Performed

- Row Count
- Duplicate Count
- Null Count
- Data Health Report
- Pipeline Logging

The SQL queries used for these checks are stored in:

`sql/ddq.sql`

---

## Example Data Health Report

    ==============================
          DATA HEALTH REPORT
    ==============================
    Rows Loaded      : 10,000,000
    Duplicates       : 607,571
    Null Values      : 0
    Pipeline Status  : SUCCESS
    ==============================

Duplicates are identified during the DDQ stage and removed during the cleaning stage.

---

## Repository Structure

    nyc-taxi-data-pipeline/
    │
    ├── data/
    ├── output/
    ├── python/
    │   ├── data_loader.py
    │   ├── data_cleaning.py
    │   ├── ddq.py
    │   ├── helper_functions.py
    │   ├── logger.py
    │   └── alert_email.py
    │
    ├── sql/
    │   ├── create_tables.sql
    │   ├── validation_queries.sql
    │   └── ddq.sql
    │
    ├── niagara/
    │   └── pipeline_steps.txt
    │
    ├── run_file.py
    ├── requirements.txt
    └── README.md

---

## Technologies Used

- Python
- Pandas
- SQL
- Google Colab
- Git
- GitHub
