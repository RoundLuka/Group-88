--select * from employees;

----SELECT Departmentid, SUM(Salary) AS TotalSalary
----FROM Employees
----GROUP BY Departmentid;

select ManagerId, SUM(Salary) as Manager_Budget from employees 
group by ManagerId

--select * from Employees
--select * from cars
--select * from Departments
--select * from customers

--select * from employees join Departments on employees.DepartmentId = Departments.Id 

