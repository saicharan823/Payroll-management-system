import sqlite3

conn = sqlite3.connect('pms.db')

cur = conn.cursor()

class Employee:
    def empinsert(self,**k):
        cur.execute(f''' insert into Employee_Details values
        ({k['EmployeeID']},"{k['Employee_Name']}",{k['DepartmentID']},"{k['Designation']}","{k['Email']}",{k['Contact_No']})
        ''')
        conn.commit()