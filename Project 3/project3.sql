CREATE DATABASE DataAnalytics_Project3;
USE DataAnalytics_Project3;
SELECT COUNT(*) AS Total_Records
FROM orders;
SELECT * FROM orders
LIMIT 5;
SHOW TABLES;
SELECT * FROM orders;
SELECT Product, COUNT(*) AS Total_Orders
FROM orders
GROUP BY Product;
SELECT Product, SUM(TotalPrice) AS Total_Sales
FROM orders
GROUP BY Product;
SELECT Product, AVG(TotalPrice) AS Average_Sales
FROM orders
GROUP BY Product;
SELECT DISTINCT OrderStatus
FROM orders;
SELECT * FROM orders
WHERE OrderStatus = 'Shipped';
SELECT * FROM orders
ORDER BY TotalPrice DESC
LIMIT 10;
SELECT * FROM orders
ORDER BY TotalPrice ASC
LIMIT 10;
SELECT PaymentMethod, SUM(TotalPrice) AS Total_Sales
FROM orders
GROUP BY PaymentMethod;
SELECT OrderStatus, COUNT(*) AS Total_Orders
FROM orders
GROUP BY OrderStatus;