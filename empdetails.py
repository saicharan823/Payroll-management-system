import sqlite3




class Employee:
    def empinsert(self,**k):
        
        conn = sqlite3.connect('pms.db')

        cur = conn.cursor()
        cur.execute(f''' insert into Employee_Details values
        ({k['EmployeeID']},"{k['Employee_Name']}",{k['DepartmentID']},"{k['Designation']}","{k['Email']}",{k['Contact_No']})
        ''')
        conn.commit()

    def show_employees(self):
        conn = sqlite3.connect('pms.db')
        cur = conn.cursor()
        cur.execute("select * from Employee_Details")
        data = []
        for i in cur.fetchall():
            context = {}
            context['employeeID'] = i[0]
            context['employeeName'] = i[1]
            context['DepartmentID'] = i[2]
            context['Designation'] = i[3]
            context['Email'] = i[4]
            context['contactNo'] = i[5]
            data.append(context)
        return data
    
    def attedance(self,**k):
        conn = sqlite3.connect('pms.db')
        cur = conn.cursor()
        cur.execute(f''' insert into Attendence values
        ({k['DepartmentID']},"{k['Department_Name']}",{k['EmployeeID']},"{k['Employee_name']}","{k['Date']}",
        "{k['Time_In']}","{k['Time_Out']}")
        ''')
        conn.commit()

    def salary(self,**k):
        conn = sqlite3.connect('pms.db')
        cur = conn.cursor()
        cur.execute(f'''insert into Salary_Details values
        ({k['EmployeeID']},{k['DepartmentID']},{k['Account_No']},"{k['PAN']}",{k['Basic_Salary']})''')
        conn.commit()

class SalaryCalculator:
    def Salarycalculation(self,EmployeeID):
        conn = sqlite3.connect('pms.db')
        cur = conn.cursor()
        cur.execute(f"select Basic_Salary from Salary_Details  where EmployeeID = {EmployeeID}")
        bs = cur.fetchall()[0][0]
        cur.execute(f"select Date,Time_In,Time_Out from Attendence where EmployeeID = {EmployeeID}")
        gt = cur.fetchall()
        print(bs)
        print(gt)
        hrs = bs/(22*8)
        su = 0
        for i in gt:
            g = (int(i[2][:2])-int(i[1][:2]))*hrs
            su = su+g
        return su



