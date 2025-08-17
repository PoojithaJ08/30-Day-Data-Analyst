# Day 04 – Retail Inventory Optimization & Demand Forecasting

## Project Title:
**Retail Inventory Optimization & Demand Forecasting using SQL, Python, Power BI, and Excel**

---

## Objective:
To optimize product inventory by forecasting demand, identifying stock risks, analyzing sales trends, and uncovering patterns influenced by pricing, promotions, and weather conditions. This helps reduce stockouts and overstocking in retail environments.

---

## Tools & Technologies Used:
- **SQL (MySQL Workbench):** Demand forecasting queries, stock analysis, revenue & discount calculations
- **Python (pandas, matplotlib, Prophet):** Data merging, cleaning, EDA, and time-series forecasting
- **Power BI:** Visual dashboards for trends, risk alerts, and KPIs
- **Excel:** Pivot tables, ABC classification, and business impact summary

---

## Dataset Info:
- **File:** `retail_store_inventory.csv`
- **Rows:** ~5,000+
- **Key Columns:** Product ID, Store ID, Units Sold, Inventory Level, Demand Forecast, Discount, Competitor Pricing, Weather, Seasonality, Promotion

---

## Business Questions Answered:
1. Which products and stores are at risk of running out of stock?
2. How accurate are current demand forecasts by SKU and store?
3. What role do promotions, discounts, and weather play in sales?
4. How is inventory turnover performing across regions?
5. Which product categories generate the most/least revenue?

---

## Key Insights:
- 🚨 22 SKUs had <5 days of stock left based on demand trends  
- 📈 Promotions improved unit sales by ~22% on average  
- 🌧️ Rainy and cloudy days correlated with reduced sales  
- 💸 Discount-heavy items made up over 35% of total revenue  
- 🔍 Electronics in the South region had the highest forecast error  

---

## SQL Summary:
- Stock coverage per product and store
- Weekly sales and inventory comparisons
- Forecast vs. actual demand gap
- Category and region-wise revenue
- Discount and competitor pricing impact

---

## Python EDA Summary:
- Cleaned and merged multi-table dataset
- Weekly trends, top SKUs, seasonal patterns
- Prophet model for 30-day sales forecast
- Identified forecast bias and over/underperformers

---

## Power BI Dashboard Includes:
- ✅ Stock Risk Table (Inventory Days < 5)
- ✅ Weekly Ordered vs. Sold Line Chart
- ✅ Category and Region Revenue Breakdown
- ✅ Forecast vs. Actual Scatter Plot
- ✅ Filters: Promotion, Region, Category, Weather
- ✅ KPI Cards: Total Units Sold, Revenue, Forecast Error, Discount %

---

## Excel Deliverables:
- Pivot Table: Units Sold by Category and Store
- Chart: ABC Inventory Classification
- Revenue & Stock Trend Line Charts
- Conditional formatting to highlight low-stock products

---

## Challenges Faced & Solutions:
| Problem | Solution |
|--------|----------|
| WEEK aggregation in SQL | Used `STR_TO_DATE()` and `WEEK()` functions |
| Column mismatch on import | Cleaned headers with `pandas` |
| ZeroDivision error in coverage calc | Used `NULLIF()` for safe division |
| Power BI slow refresh | Pre-aggregated data using Python |

---

## Value Delivered:
- Helped retail team detect stock risks early
- Highlighted low-performing products for markdown
- Uncovered price sensitivity and weather-based demand shifts
- Boosted confidence in demand planning strategy

---

## Learnings:
- Integrated SQL, Python, Power BI, and Excel end-to-end
- Automated forecasting with Prophet for SKUs
- Performed ABC analysis and created insight-driven dashboards
- Managed multiple influencing factors like discounts, competitors, and events

---

## Use Case:
This project is ideal for retail operations managers, supply chain analysts, or business teams looking to forecast demand accurately and optimize inventory management.

---

