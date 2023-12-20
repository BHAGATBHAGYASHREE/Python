class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, gender, city):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.gender = gender
        self.city = city

    def display_employee_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_salary}")
        print(f"Gender: {self.gender}")
        print(f"City: {self.city}")
employee1 = Employee(emp_id=1, emp_name="Pankaj", emp_salary=55000, gender="Male", city="Delhi")
employee1.display_employee_info()
