# PowerBI-Finance-Analytics-Dashboard
# End-to-End Investment Portfolio Analytics Dashboard

This project is a comprehensive business intelligence solution designed to track, analyze, and visualize the performance of a personal stock portfolio. It covers the entire data pipeline, from automated data extraction using Python to interactive dashboarding in Power BI.

---

## 🚀 Final Dashboard

check the files***


---

## 🛠️ Technical Stack
* **Data Extraction:** Python (Pandas, yfinance)
* **Database:** MySQL
* **ETL & Data Loading:** SQL (MySQL Workbench)
* **Data Visualization & Modeling:** Power BI (DAX)

---

## 🏗️ Project Architecture
The project follows a standard data pipeline architecture:

1.  **Data Extraction (Python):** A Python script automates the process of fetching historical stock price data and benchmark information from the yfinance API. It also generates sample transaction data, saving all outputs to CSV files.

2.  **Database Storage & ETL (MySQL):** A relational database was designed in MySQL to store the data. The schema includes tables for stocks, transactions, and historical prices. A single, robust SQL script creates the database, tables, and loads the data from the CSVs using `LOAD DATA INFILE`, handling potential errors and data type issues.

3.  **Visualization (Power BI):** Power BI connects directly to the MySQL database. Data is modeled with relationships, and advanced calculations are created using DAX (Data Analysis Expressions) to derive key metrics like Total Investment, Realized P&L, and Current Portfolio Value. The final interactive dashboard allows for dynamic filtering and analysis.

---

## ✨ Key Features & Insights
* **KPI Monitoring:** Top-level cards display key metrics like Total Investment, Sales Revenue, and Net Invested Capital.
* **Portfolio Composition:** Donut and Bar charts provide a clear breakdown of investments by company and sector.
* **Performance vs. Benchmark:** A dual-axis line chart compares individual stock price trends against a market benchmark (Nifty 50).
* **Profitability Analysis:** A "Cost vs. Current Value" chart visualizes the unrealized profit for each holding.
* **Interactive Filtering:** Slicers for company and date range allow for dynamic, in-depth exploration of the entire dashboard.
