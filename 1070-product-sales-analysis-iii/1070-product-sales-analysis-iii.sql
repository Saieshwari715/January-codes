# Write your MySQL query statement below
select product_id,year as first_year,quantity,price from sales as s WHERE (s.product_id, s.year) IN (
    SELECT product_id, MIN(year)
    FROM sales
    GROUP BY product_id
);