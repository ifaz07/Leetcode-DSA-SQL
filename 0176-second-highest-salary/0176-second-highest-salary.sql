# Write your MySQL query statement below
SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1 
    -- LIMIT 1 OFFSET 0 → 9000 (highest)
    -- LIMIT 1 OFFSET 1 → 8000 (second highest)
) AS SecondHighestSalary;