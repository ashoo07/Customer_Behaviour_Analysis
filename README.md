# Customer Behaviour Analysis

An end-to-end retail analytics project: **Python** for cleaning and EDA, **PostgreSQL** for business analysis, and **Power BI** for an interactive dashboard.

The goal is to answer practical retail questions. Which categories and age groups drive revenue? Do subscribers spend more? Are discounts actually used? Which customers are loyal?


---

## Key Findings

Based on 3,900 purchase records totalling **$233,081** in revenue (average purchase: **$59.76**).

- **Revenue by category:** Clothing is the top earner at **$104,264 (44.7%)** of total revenue, followed by Accessories (31.8%), Footwear (15.5%), and Outerwear (7.9%).
- **Age groups:** revenue is spread almost evenly. Young Adults (18-31) lead slightly at **26.7%**, while the other three age bands each contribute 24-25%.
- **Subscribers vs. non-subscribers:** subscribers do **not** spend more. Average purchase is $59.49 for subscribers vs. $59.87 for non-subscribers, and only 27% of customers (1,053) are subscribed. This points to an opportunity to improve the value of the subscription offer.
- **Discounts:** **43%** of purchases used a discount. Hats (50%), Sneakers (49.7%), and Coats (49.1%) have the highest discount usage.
- **Customer segments:** **79.9%** of customers are Loyal (more than 10 previous purchases), 18.0% are Returning (2-10), and only 2.1% are New.
- **Top-rated products:** Gloves (3.86), Sandals (3.84), and Boots (3.82) have the highest average review ratings.
- **Gender:** male customers account for 67.7% of revenue.

**Business takeaway:** revenue is concentrated in Clothing and Accessories (about 77%), and spend is nearly flat across age groups and subscription status. Growth is more likely to come from retaining the large loyal base, making subscriptions more valuable, and recruiting new customers than from targeting a particular age group.

---

## Dataset

File: `customer_shopping_behavior.csv`

Each row is a customer purchase record. Fields include:

| Area | Fields |
|---|---|
| Customer | demographics (e.g. age, gender), subscription status |
| Purchase | product category, items purchased, purchase amount, previous purchases, purchase frequency |
| Behaviour | review rating, discount usage, shipping method |

3,900 records and 18 columns. Review Rating has 37 missing values, which are handled in the cleaning step.


---

## Tech Stack

| Tool | Used for |
|---|---|
| Python (Pandas, NumPy) | Data cleaning, feature engineering, EDA |
| Jupyter Notebook | Analysis environment |
| SQLAlchemy, psycopg2 | Loading cleaned data into PostgreSQL |
| PostgreSQL | Business queries |
| Power BI | Interactive dashboard |

---

## Workflow

### 1. Python: cleaning and EDA
- Loaded the dataset and checked structure, data types, and missing values
- Handled missing values and standardized column names and types
- Engineered new features:
  - **Age groups**
  - **Purchase frequency in days**
  - **Customer segments**
- Explored spending, ratings, categories, and subscriptions

### 2. PostgreSQL: business analysis
Loaded the cleaned data into PostgreSQL and wrote queries for:
- Revenue by gender and by category
- Average customer spend
- Top-rated products
- Discount usage by product
- Subscriber vs. non-subscriber spending
- Top products by purchase volume
- Customer segmentation
- Revenue contribution by age group

### 3. Power BI: dashboard
An interactive dashboard with filters, covering:
- Total revenue, total customers, average purchase amount
- Revenue by category and by age group
- Customer segments
- Subscription analysis
- Product performance
- Discount trends

---

## Repository Contents

```
Customer_Behaviour_Analysis/
├── DA Project (shopping analysis) (1).ipynb   # Python cleaning, feature engineering, EDA
├── customer_behaviour.sql                     # PostgreSQL business queries
├── customer_behaviour_dashboard.pbix          # Power BI dashboard
├── customer_shopping_behavior.csv             # Raw dataset
├── LICENSE
└── README.md
```

---

## How to Run

**1. Clone the repo**
```bash
git clone https://github.com/ashoo07/Customer_Behaviour_Analysis.git
cd Customer_Behaviour_Analysis
```

**2. Python**
```bash
pip install pandas numpy sqlalchemy psycopg2-binary jupyter
jupyter notebook
```
Open the notebook and run the cells in order. It cleans the data and prepares it for loading into PostgreSQL.

**3. PostgreSQL**
1. Create a database (e.g. `customer_behaviour`).
2. Load the cleaned dataset into a table from the notebook (via SQLAlchemy) or with your preferred import method.
3. Run `customer_behaviour.sql` to reproduce the analysis.

**4. Power BI**
1. Open `customer_behaviour_dashboard.pbix` in Power BI Desktop.
2. If prompted, update the PostgreSQL connection to point at your database.
3. Refresh the data and explore using the filters.

---

## Skills Demonstrated

Data cleaning · Feature engineering · Exploratory data analysis · SQL (PostgreSQL) · Customer segmentation · Dashboard design · Business storytelling

---

## License

Released under the [MIT License](LICENSE).
