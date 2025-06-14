-- Step 1: Filter valid transactions
SELECT *
FROM data
WHERE CustomerID IS NOT NULL
  AND InvoiceNo NOT LIKE 'C%';

WITH valid_orders AS (
    SELECT *
    FROM data
    WHERE CustomerID IS NOT NULL
      AND InvoiceNo NOT LIKE 'C%'
),

rfm_table AS (
    SELECT
        CustomerID,
        MAX(InvoiceDate) AS LastPurchaseDate,
        COUNT(DISTINCT InvoiceNo) AS Frequency,
        ROUND(SUM(Quantity * UnitPrice), 2) AS Monetary
    FROM valid_orders
    GROUP BY CustomerID
)

SELECT 
    CustomerID,
    DATEDIFF('2011-12-10', LastPurchaseDate) AS Recency,
    Frequency,
    Monetary
FROM rfm_table;
