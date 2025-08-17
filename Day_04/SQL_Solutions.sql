
-- 1. Top 10 Best-Selling Products
SELECT `Product ID`, SUM(`Units Sold`) AS total_units_sold
FROM retail_store_inventory
GROUP BY `Product ID`
ORDER BY total_units_sold DESC
LIMIT 10;

-- 2. Daily Sales Trend
SELECT `Date`, SUM(`Units Sold`) AS daily_units_sold
FROM retail_store_inventory
GROUP BY `Date`
ORDER BY `Date`;

-- 3. Average Daily Sales per Product
SELECT `Product ID`, ROUND(AVG(`Units Sold`), 2) AS avg_units_sold
FROM retail_store_inventory
GROUP BY `Product ID`
ORDER BY avg_units_sold DESC;

-- 4. Products at Risk of Stockout (Stock < 5 Days)
WITH avg_sales AS (
  SELECT `Product ID`, `Store ID`, AVG(`Units Sold`) AS avg_daily
  FROM retail_store_inventory
  GROUP BY `Product ID`, `Store ID`
)
SELECT r.`Product ID`, r.`Store ID`, r.`Inventory Level`,
       ROUND(r.`Inventory Level` / NULLIF(a.avg_daily, 0), 2) AS stock_days_left
FROM retail_store_inventory r
JOIN avg_sales a
  ON r.`Product ID` = a.`Product ID` AND r.`Store ID` = a.`Store ID`
WHERE ROUND(r.`Inventory Level` / NULLIF(a.avg_daily, 0), 2) < 5;

-- 5. Inventory Turnover Ratio by Store
SELECT `Store ID`,
       ROUND(SUM(`Units Sold`) / NULLIF(AVG(`Inventory Level`), 0), 2) AS inventory_turnover_ratio
FROM retail_store_inventory
GROUP BY `Store ID`
ORDER BY inventory_turnover_ratio DESC;

-- 6. Total Revenue by Category & Region
SELECT `Category`, `Region`,
       SUM(`Units Sold` * `Price` * (1 - `Discount` / 100)) AS total_revenue
FROM retail_store_inventory
GROUP BY `Category`, `Region`
ORDER BY total_revenue DESC;

-- 7. Weekly Units Ordered vs. Sold
SELECT DATE_FORMAT(`Date`, '%Y-%u') AS week,
       SUM(`Units Ordered`) AS total_ordered,
       SUM(`Units Sold`) AS total_sold
FROM retail_store_inventory
GROUP BY week
ORDER BY week;

-- 8. Product-Store Forecast Gap (Over/Under Forecasting)
SELECT `Product ID`, `Store ID`,
       SUM(`Units Sold`) AS actual_sold,
       SUM(`Demand Forecast`) AS forecasted,
       SUM(`Units Sold`) - SUM(`Demand Forecast`) AS forecast_error
FROM retail_store_inventory
GROUP BY `Product ID`, `Store ID`
ORDER BY forecast_error DESC;

-- 9. Total Units Sold per Category
SELECT `Category`, SUM(`Units Sold`) AS total_units_sold
FROM retail_store_inventory
GROUP BY `Category`
ORDER BY total_units_sold DESC;

-- 10. Revenue by Product ID with Discounts Applied
SELECT `Product ID`,
       SUM(`Units Sold` * `Price` * (1 - `Discount`/100)) AS total_revenue
FROM retail_store_inventory
GROUP BY `Product ID`
ORDER BY total_revenue DESC;

-- 11. Weekly Sales Trend by Region
SELECT DATE_FORMAT(`Date`, '%Y-%u') AS week, `Region`, SUM(`Units Sold`) AS weekly_units_sold
FROM retail_store_inventory
GROUP BY week, `Region`
ORDER BY week, `Region`;

-- 12. Stock Coverage in Days per Store-Product
WITH avg_sales AS (
  SELECT `Product ID`, `Store ID`, AVG(`Units Sold`) AS avg_daily
  FROM retail_store_inventory
  GROUP BY `Product ID`, `Store ID`
)
SELECT r.`Store ID`, r.`Product ID`, r.`Inventory Level`, a.avg_daily,
       ROUND(r.`Inventory Level` / NULLIF(a.avg_daily, 0), 2) AS days_coverage
FROM retail_store_inventory r
JOIN avg_sales a
  ON r.`Product ID` = a.`Product ID` AND r.`Store ID` = a.`Store ID`
WHERE ROUND(r.`Inventory Level` / NULLIF(a.avg_daily, 0), 2) < 5;

-- 13. Promotion vs Non-Promotion Sales Comparison
SELECT `Holiday/Promotion`, AVG(`Units Sold`) AS avg_units_sold,
       AVG(`Units Ordered`) AS avg_units_ordered
FROM retail_store_inventory
GROUP BY `Holiday/Promotion`;

-- 14. Impact of Weather on Units Sold
SELECT `Weather Condition`, AVG(`Units Sold`) AS avg_units_sold
FROM retail_store_inventory
GROUP BY `Weather Condition`
ORDER BY avg_units_sold DESC;

-- 15. Sales Variance by Seasonality
SELECT `Seasonality`, SUM(`Units Sold`) AS total_units, 
       SUM(`Units Sold` * `Price`) AS gross_sales
FROM retail_store_inventory
GROUP BY `Seasonality`
ORDER BY total_units DESC;

-- 16. Competitor Price Impact
SELECT `Product ID`, ROUND(AVG(`Price` - `Competitor Pricing`), 2) AS avg_price_gap,
       ROUND(AVG(`Units Sold`), 2) AS avg_units_sold
FROM retail_store_inventory
GROUP BY `Product ID`
ORDER BY avg_price_gap DESC;

-- 17. Forecast Accuracy by Store-Product
SELECT `Store ID`, `Product ID`,
       SUM(`Units Sold`) AS actual_sold,
       SUM(`Demand Forecast`) AS forecasted,
       ROUND(SUM(`Units Sold`) - SUM(`Demand Forecast`), 2) AS forecast_error
FROM retail_store_inventory
GROUP BY `Store ID`, `Product ID`
ORDER BY forecast_error DESC;

-- 18. Total Discount Given per Category
SELECT `Category`, SUM(`Units Sold` * `Price` * (`Discount`/100)) AS total_discount_given
FROM retail_store_inventory
GROUP BY `Category`
ORDER BY total_discount_given DESC;
