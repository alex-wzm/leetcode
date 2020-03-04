-- Write your MySQL query statement below
SELECT name as "Employee"
FROM employee as e1
WHERE salary > (
    SELECT salary
    FROM employee as e2
    WHERE e2.id=e1.managerid
);

-- LeetCode Approach 1: Using WHERE clause (Accepted)
SELECT e1.Name AS 'Employee'
FROM
    Employee AS e1,
    Employee AS e2
WHERE e1.ManagerId = e2.Id
    AND e1.Salary > e2.Salary
;

-- LeetCode Approach 2: Using JOIN clause (Accepted)
SELECT e1.NAME AS Employee
FROM Employee AS e1
JOIN Employee AS e2
    ON e1.ManagerId = e2.Id
        AND e1.Salary > e2.Salary
;