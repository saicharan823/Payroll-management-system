from empdetails import Employee
from empdetails import SalaryCalculator
from flask import Flask,render_template,jsonify,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/employee_signup', methods=['GET','POST'])
def process_signup():
    if request.method == 'POST':
        employeeId = request.form.get('employeeId')
        employeeName = request.form.get('employeeName')
        departmentId = request.form.get('departmentId')
        designation = request.form.get('designation')
        email = request.form.get('email')
        contactNo = request.form.get('contactNo')
        print(employeeId,employeeName,designation)
        emp = Employee()
        emp.empinsert(EmployeeID = employeeId,Employee_Name=employeeName,DepartmentID= departmentId,Designation=designation,
        Email= email,Contact_No=contactNo)
        return jsonify({'Message':"successfully fetched the data"})
    else:
        return render_template('signup.html')

@app.route('/employees', methods = ['GET','POST'])
def show_employees():
    emp = Employee()
    data = emp.show_employees()
    print(data)
    return render_template('showemployees.html',employees=data)

@app.route('/attendance', methods = ['GET','POST'])
def attendance():
    if request.method=='POST':
        dptId = request.form.get('DepartmentID')
        dptName = request.form.get('DepartmentName')
        empId = request.form.get('EmployeeID')
        empName = request.form.get('EmployeeName')
        date = request.form.get('Date')
        TimeIn = request.form.get('TimeIn')
        TimeOut = request.form.get('TimeOut')
        print(dptId,dptName)
        emp = Employee()
        emp.attedance(DepartmentID=dptId,Department_Name=dptName,
        EmployeeID=empId,Employee_name=empName,Date=date,Time_In=TimeIn,Time_Out=TimeOut)
        return jsonify({'Message':"Successfully data fetched"})
    else:
        return render_template('attendance.html')

@app.route('/payroll_release', methods = ['GET','POST'])
def Salary():
    if request.method=='POST':
        empId = request.form.get('employeeID')
        dptId = request.form.get('departmentID')
        acc_no = request.form.get('accountNo')
        pan = request.form.get('PAN')
        Basicsalary = request.form.get('basicSalary')
        print(empId)
        emp = Employee()
        emp.salary(EmployeeID = empId,DepartmentID = dptId,Account_No = acc_no,PAN = pan,Basic_Salary = Basicsalary)
        return jsonify({'Meassage':"Sucessfully data fetched"})
    else:
        return render_template('Payroll.html')

@app.route('/attendance_report', methods = ['GET','POST'])
def salary_release():
    if request.method=='POST':
        empid=request.form.get('employee_id')
        sc = SalaryCalculator()
        total_sallary=sc.Salarycalculation(EmployeeID=int(empid))
        context = {'EmployeeID':empid,'TotalSalary':int(total_sallary)}
        return render_template('showsalary.html',data=context)
    else:
        return render_template('empid.html')
        






    

if __name__== '__main__':
    app.run(host = '0.0.0.0', port = 5050)




























