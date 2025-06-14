# Day_02 Project: Customer Segmentation Using RFM Analysis

##  Project Title:
**Customer Segmentation Using RFM Analysis**

## Problem Statement:
The company wants to understand its customer base and segment users based on their purchasing behavior. The aim is to use RFM (Recency, Frequency, Monetary) analysis to categorize customers into different groups such as loyal, at-risk, or high-value.

## Tools Used:
- **SQL** – To extract customer transaction summaries  
- **Python** – For RFM scoring and data preprocessing  
- **Power BI** – Interactive dashboard showing segments  
- **Excel** – Quick summary of RFM segments using pivot tables

## Key Insights:
- High-value customers made recent, frequent, and high-spending purchases  
- About 18% of customers fell into the "Champions" segment  
- Nearly 25% of customers are at risk due to low recency and frequency  
- Loyal customers have high frequency but moderate monetary value  

## Challenges Faced:
- Handling missing CustomerIDs and incomplete/canceled transactions  
- Converting datetime to usable recency values  
- Normalizing metrics across thousands of customers for scoring

## Solutions Implemented:
- Filtered out null `CustomerID` and canceled invoices  
- Used max transaction date per customer to compute recency  
- Applied quantile-based scoring (1 to 4) for R, F, M  
- Combined RFM scores into customer segments using a rule-based system

---

## Power BI Dashboard:

> _Screenshot Placeholder Below_

**// Insert Power BI dashboard screenshot here //**

### Visual Breakdown:
- **Pie Chart**: Distribution of customer segments (Champions, At Risk, Loyal, etc.)
- **Bar Chart**: Average monetary value by segment
- **Table**: Top 10 high-value customers (sorted by monetary value)
- **Filters**: Recency range, Frequency range, Segment selector

---

