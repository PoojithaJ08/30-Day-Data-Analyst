
-- Day_03 – Rossmann Sales Forecasting and Store Performance Analysis
-- ================================================

-- 🟢 1. Total Sales and Customers by Store
SELECT Store, SUM(Sales) AS Total_Sales, SUM(Customers) AS Total_Customers
FROM Rossmann
GROUP BY Store
ORDER BY Total_Sales DESC;

-- 🟢 2. Average Sales by StoreType
SELECT StoreType, ROUND(AVG(Sales), 2) AS Avg_Sales
FROM Rossmann
GROUP BY StoreType
ORDER BY Avg_Sales DESC;

-- 🟢 3. Impact of Promotions on Sales
SELECT Promo, ROUND(AVG(Sales), 2) AS Avg_Sales
FROM Rossmann
GROUP BY Promo;

-- 🟢 4. Sales Performance During School Holidays
SELECT SchoolHoliday, ROUND(AVG(Sales), 2) AS Avg_Sales
FROM Rossmann
GROUP BY SchoolHoliday;

-- 🟢 5. Monthly Sales Trends
SELECT 
    YEAR(Date) AS Year, 
    MONTH(Date) AS Month, 
    SUM(Sales) AS Monthly_Sales
FROM Rossmann
GROUP BY YEAR(Date), MONTH(Date)
ORDER BY Year, Month;

-- 🟢 6. Top 10 Performing Stores by Average Sales
SELECT Store, ROUND(AVG(Sales), 2) AS Avg_Sales
FROM Rossmann
GROUP BY Store
ORDER BY Avg_Sales DESC
LIMIT 10;

-- 🟢 7. Competition Distance vs Average Sales
SELECT 
    CASE 
        WHEN CompetitionDistance < 500 THEN 'Near'
        WHEN CompetitionDistance BETWEEN 500 AND 1500 THEN 'Medium'
        ELSE 'Far'
    END AS Competition_Proximity,
    ROUND(AVG(Sales), 2) AS Avg_Sales
FROM Rossmann
GROUP BY Competition_Proximity;

-- 🟢 8. StoreType & Promo Combined Effect
SELECT StoreType, Promo, ROUND(AVG(Sales), 2) AS Avg_Sales
FROM Rossmann
GROUP BY StoreType, Promo
ORDER BY StoreType, Promo;

-- 🟢 9. Assortment Type vs Sales
SELECT Assortment, ROUND(AVG(Sales), 2) AS Avg_Sales
FROM Rossmann
GROUP BY Assortment
ORDER BY Avg_Sales DESC;

-- 🟢 10. Number of Days Store Was Open vs Closed
SELECT Open, COUNT(*) AS Count_Days
FROM Rossmann
GROUP BY Open;

-- ✅ End of SQL Solutions
