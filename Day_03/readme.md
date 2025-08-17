# Day_03 – Rossmann Sales Forecasting and Store Performance Analysis

##  Project Title:
**Rossmann Sales Forecasting and Store Performance Analysis**

---

##  Problem Statement:
Rossmann, a large drug store chain, wants to understand its sales patterns across different store types, regions, and time periods. The company also wants to assess the impact of promotions and holidays on store performance to improve inventory planning and promotional strategies. This analysis aims to uncover patterns, trends, and actionable insights using historical sales data.

---

##  Tools & Technologies Used:
- **SQL (MySQL Workbench):** Querying store-wise performance, holiday impacts, and average sales by store type
- **Python (Pandas, Seaborn, Matplotlib):** Data cleaning, feature engineering, EDA, visualizations
- **Power BI:** Interactive dashboard with store filters, KPI cards, and trend lines
- **Excel:** Pivot tables and charts to support quick slice-and-dice analysis

---

##  Dataset Overview:
- **File:** `Rossmann.csv`
- **Size:** ~100,000 rows
- **Key Columns:**  
  - `Store`, `Date`, `Sales`, `Customers`, `Open`, `Promo`, `SchoolHoliday`, `StateHoliday`, `StoreType`, `Assortment`, `CompetitionDistance`

---

## Business Questions Answered:
1. Which **store types** and **assortments** yield the highest average sales?
2. How do **promotions**, **school holidays**, and **state holidays** affect store performance?
3. Is there a visible **seasonality or trend** in sales across months and years?
4. Which stores are **most/least dependent** on promotional activities?
5. How does **competition distance** impact store sales?

---

##  Key Insights:
- **Store Type A** consistently has the highest average sales and customer count.
- **Promotions** significantly increase sales—especially during non-holiday weeks.
- **School holidays** slightly reduce sales in city-centric stores but increase in suburban areas.
- **December** shows peak sales activity across almost all stores (seasonal holiday effect).
- **Competition Distance** plays a moderate role—closer competitors correlate with slightly lower sales.

---

## Power BI Dashboard Features:
- KPI Cards: Total Sales, Customers, Avg Sales/Store
- Filters: Store Type, Promo, Assortment, School Holiday
- Line Charts: Monthly Sales Trends
- Bar Charts: Top 10 Stores by Sales
- Slicers: Dynamic control by holiday flags and promotions

---

##  Excel Insights:
- Pivot tables by StoreType and Month
- Conditional formatting for negative trends
- Store-wise ranking by average monthly sales

---

##  Challenges Faced & Solutions:
| Challenge | Solution |
|----------|----------|
| Missing data on holidays and promotions | Used forward-fill and median imputation |
| Date format inconsistencies | Converted all dates to datetime format in Python |
| High variance in sales across stores | Normalized by store and used log transformation where necessary |
| Complex relationships between holiday and promo effects | Created interaction terms in Python for better pattern recognition |

---

##  Business Impact:
This analysis helps Rossmann:
- Target high-performing stores for new product launches
- Schedule staff more efficiently during high-traffic months
- Plan more effective and timely promotions
- Evaluate competitor proximity as a factor in new store openings

---
