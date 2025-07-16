# Day 01 – Sales Performance Analysis


## Project Title:
**Retail Sales Performance Analysis using SQL, Python, Power BI, and Excel**

---

## Objective:
To analyze Superstore sales data across multiple dimensions (geography, category, time, customer segments) and derive actionable insights to improve profitability, inventory planning, and regional sales strategy.

---

## Tools & Technologies Used:
- **SQL (MySQL Workbench):** Structured queries, aggregations, and business KPIs
- **Python (pandas, matplotlib):** Data cleaning, exploratory data analysis (EDA), visualizations
- **Power BI:** Dynamic dashboard with slicers, KPIs, and charts
- **Excel:** Pivot tables and basic summary analysis

---

## Dataset Info:
- **File:** `Superstore_clean.csv`
- **Rows:** ~10,000+
- **Key Columns:** Sales, Profit, Category, Sub-Category, State, Region, Segment, Ship Mode, Order Date

---

##  Business Questions Answered:
1. Which states and cities generate the most profit and sales?
2. What categories or sub-categories are losing money?
3. When do sales peak across the year?
4. Which segments or regions are most profitable?
5. How does ship mode affect sales and cost?

---

## Key Insights:
-  **California, New York, and Texas** lead in revenue; California also has high losses due to discount-heavy items.
- **Tables, Bookcases, and Supplies** sub-categories have low or negative profits.
- **Q4 months (Nov–Dec)** see peak sales activity, suggesting seasonal shopping patterns.
- **Corporate segment** performs better than Consumer in most regions.
- **Standard Class** is the most used shipping method but not always profitable.

---

## SQL Summary:
- Top 10 states by profit
- Worst 5 categories by profit margin
- Month-wise sales and profit
- Segment and region analysis
- Orders with negative profit

---

## Python EDA Summary:
- Loaded and cleaned dataset using `pandas`
- Checked null values, data types, and distributions
- Created bar plots, histograms, and trend lines
- Exported clean data for Power BI and MySQL use

---

## Power BI Dashboard Includes:
- ✅ 4 KPI Cards: Sales, Profit, Quantity, Discount
- ✅ Sales by State: Map visual
- ✅ Monthly Trend: Line chart
- ✅ Category/Sub-Category: Stacked bar chart
- ✅ Ship Mode: Treemap
- ✅ Filters/Slicers: Region, Segment, Category
- ✅ Profit Matrix: Segment vs Region heatmap

---

## Excel Deliverables:
- Pivot Table: Region vs Category Profit
- Charts: Top categories by sales and loss
- Conditional formatting to highlight low-margin segments

---

## Challenges Faced & Solutions:
| Problem | Solution |
|--------|----------|
| Encoding issue while reading CSV | Used `encoding='latin1'` |
| SQL `LOAD DATA` permission error | Used Import Wizard in MySQL |
| Column name mismatches | Cleaned headers in Python |
| Date parsing errors in Power BI | Used cleaned date column from Python |

---

## Value Delivered:
- Helped identify **underperforming products**
- Guided focus on **profitable states and segments**
- Pinpointed **seasonal trends** to optimize inventory

---

## Learnings:
- Performed full-cycle analysis from raw data to insights
- Built storytelling dashboards with real business KPIs
- Strengthened understanding of SQL joins, filters, and groupings
- Learned how to clean and export data effectively across tools

---

## Use Case:
This project is ideal for retail sales teams, regional managers, or data-driven executives who want to make strategic decisions using historical performance data.

---

