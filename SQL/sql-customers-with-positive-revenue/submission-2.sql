-- Write your query below
select customer_id from (select customer_id,sum(revenue) as rvn from customers where year = 2020 group by customer_id, year) where rvn>0