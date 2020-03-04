-- Write your MySQL query statement below
SELECT name as "Employee"
FROM employee as e1
WHERE salary > (
    SELECT salary
    FROM employee as e2
    WHERE e2.id=e1.managerid
);