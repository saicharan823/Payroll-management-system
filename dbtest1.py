
from empdetails import Employee
emp = Employee()

'''emp.empinsert(EmployeeID = 1,Employee_Name='xyz',DepartmentID=1,Designation='manager',Email='xyz@gmail.com',Contact_No=8328119803)'''

'''emp.attedance(DepartmentID=8,Department_Name='csk',EmployeeID=23,Employee_name='sai',Date='18/07/2023',Time_In='12:54',Time_Out='5:30')

"""emp.salary(EmployeeID=10,DepartmentID=20,Account_No=12345,PAN='BGLPC098',Basic_Salary=12890)

Salary = (time_out - time_in) * hourly_wage

Salary = days_worked * daily_rate'''

import sqlite3
conn = sqlite3.connect('pms.db')

cur = conn.cursor()




from empdetails import SalaryCalculator

sal = SalaryCalculator()

sal.Salarycalculation(EmployeeID=1)



