-- Write your query below
select employee_id,
CASE 
WHEN employee_id %2 != 0 AND NAME NOT LIKE 'M%'
THEN salary
ELSE 0
END AS 
bonus from EMPLOYEES ORDER BY EMPLOYEES 