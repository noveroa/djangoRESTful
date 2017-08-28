SELECT * FROM BucketList.employee;

SELECT * From BucketList.Department;


##############################################################
##############################################################
# return record of the top earner
# v.A
SELECT * From BucketList.employee e
ORDER BY salary DESC LIMIT 1;
# v.B
SELECT *
FROM BucketList.employee e
WHERE salary = (select MAX(salary) from BucketList.employee);
##############################################################
##############################################################
# select max salary
SELECT MAX(salary)  from BucketList.employee;
##############################################################
##############################################################
# return record of the 2nd highest salary
SELECT * FROM  BucketList.employee e
WHERE  salary =
	( 	SELECT MAX(salary)
		FROM  BucketList.employee e
		WHERE
			salary NOT IN (SELECT  MAX(salary) from BucketList.employee e
            )
	);
##############################################################
##############################################################
#select range of employees based on id
SELECT *
FROM  BucketList.employee e
WHERE e.Employee_id BETWEEN 2003 AND 2008;
##############################################################
##############################################################
#Return highest paid employee, name, id salary and department
SELECT
CONCAT(e. first_name,  '  ', e. last_name ) as 'Full Name',
e.salary,
d.department_name,
e.department_id
FROM BucketList.employee e
INNER JOIN BucketList.Department d
ON e.department_id = d.department_id
WHERE e.salary = (select MAX(salary) from BucketList.employee);
##############################################################
#############################################################
#Return highest paid employee, name, id salary and department FROM EACH department
SELECT
CONCAT(e. first_name,  '  ', e. last_name ) as 'Full Name',
e.salary,
d.department_name,
e.department_id
FROM BucketList.employee e
INNER JOIN BucketList.Department d
ON e.department_id = d.department_id
WHERE salary IN  (
		SELECT MAX(salary)
		FROM BucketList.employee
        GROUP BY department_id)

##############################################################