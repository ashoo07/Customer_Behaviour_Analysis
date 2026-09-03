# Customer_Behaviour_Analysis
Developed an end-to-end Customer Behaviour Analysis project using Python, SQL, and Power BI. Cleaned and transformed retail data, analyzed customer segments, purchasing patterns, product performance, discounts, and revenue trends, and built an interactive dashboard to generate actionable business insights.

# Customer Behaviour Analysis

## Overview

**Customer Behaviour Analysis** is an end-to-end data analytics project focused on understanding retail customer purchasing patterns, product performance, customer segments, discounts, and revenue trends.

The project follows a real-world analytics workflow using **Python for data preparation and EDA, PostgreSQL for business analysis, and Power BI for interactive visualization**.

---

## Dataset

The dataset contains retail customer and transaction-level information, including:

* Customer demographics
* Product categories
* Items purchased
* Purchase amounts
* Review ratings
* Subscription status
* Discount usage
* Shipping methods
* Previous purchases
* Purchase frequency

---

## Tools & Technologies

* **Python** – Data cleaning, transformation & EDA
* **Pandas & NumPy** – Data manipulation and analysis
* **PostgreSQL** – SQL-based business analysis
* **Power BI** – Interactive dashboard & visualization
* **Jupyter Notebook** – Python analysis environment

---

## Project Steps

### 1. Data Loading

* Loaded the retail dataset into Python using Pandas.
* Examined dataset structure, columns, data types, and missing values.

### 2. Exploratory Data Analysis

* Analyzed customer demographics and purchasing behavior.
* Identified patterns in product categories, spending, ratings, and subscriptions.

### 3. Data Cleaning & Transformation

* Handled missing values.
* Standardized column names and data types.
* Created additional features such as:

  * Age Groups
  * Purchase Frequency in Days
  * Customer Segments

### 4. PostgreSQL Analysis

Loaded the cleaned dataset into PostgreSQL and performed business-focused SQL analysis, including:

* Revenue by gender and category
* Average customer spending
* Top-rated products
* Discount usage by product
* Subscriber vs. non-subscriber spending
* Top products by purchase volume
* Customer segmentation
* Revenue contribution by age group

### 5. Power BI Dashboard

Created an interactive dashboard to visualize key business metrics and customer behavior.

---

## Dashboard

The Power BI dashboard provides insights into:

* **Total Revenue**
* **Total Customers**
* **Average Purchase Amount**
* **Revenue by Category**
* **Customer Segments**
* **Subscription Analysis**
* **Product Performance**
* **Discount Trends**
* **Age Group Revenue**

Filters and interactive visuals allow users to explore customer behavior from different perspectives.

---

## Key Results

The analysis helps identify:

* High-performing product categories
* Products with strong purchase demand
* Differences between subscribed and non-subscribed customers
* Customer segments based on purchase history
* Discount patterns across products
* Revenue contribution across different age groups
* Customer purchasing and spending trends

These insights can support **retail sales strategy, customer retention, promotional planning, and product decisions**.

---

## How to Run

### Python

Install the required libraries:

```bash
pip install pandas numpy sqlalchemy psycopg2-binary
```

Load the dataset:

```python
import pandas as pd

df = pd.read_csv("customer_shopping_behavior.csv")
```

Perform data cleaning and analysis using the provided Jupyter Notebook.

### PostgreSQL

1. Create a PostgreSQL database.
2. Load the cleaned dataset into PostgreSQL.
3. Run the SQL queries provided in the project.
4. Use the query results for business analysis.

### Power BI

1. Open the Power BI `.pbix` file.
2. Connect to the PostgreSQL database if required.
3. Refresh the data.
4. Interact with the dashboard using available filters and visuals.

---

## Project Structure

```text
Customer_Behaviour_Analysis/
│
├── data/
│   └── customer_shopping_behavior.csv
│
├── python/
│   └── customer_behavior_analysis.ipynb
│
├── sql/
│   └── customer_behavior_analysis.sql
│
├── powerbi/
│   └── customer_behavior_dashboard.pbix
│
└── README.md
```

---

## Skills Demonstrated

**Python | Pandas | NumPy | SQL | PostgreSQL | Data Cleaning | EDA | Data Transformation | Data Analysis | Power BI | Data Visualization | Business Insights**
