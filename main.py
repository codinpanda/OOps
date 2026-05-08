import csv
import os

class Employee:
    def __init__(self, emp_id, name, department):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.__salary = 0 

    def set_salary(self, amount):
        if amount >= 0:
            self.__salary = amount
        else:
            raise ValueError("Salary cannot be negative.")

    def get_salary(self):
        return self.__salary

    def calculate_salary(self):

        return self.get_salary()

    def __str__(self):
        return f"[{self.emp_id}] {self.name} (Dept: {self.department}) - {self.__class__.__name__}"


class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, department, monthly_salary):
        super().__init__(emp_id, name, department)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        self.set_salary(self.monthly_salary)
        return self.get_salary()


class Intern(Employee):
    def __init__(self, emp_id, name, department, stipend):
        super().__init__(emp_id, name, department)
        self.stipend = stipend

    def calculate_salary(self):
        self.set_salary(self.stipend)
        return self.get_salary()


class Contractor(Employee):
    def __init__(self, emp_id, name, department, hourly_rate, hours_worked):
        super().__init__(emp_id, name, department)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        self.set_salary(self.hourly_rate * self.hours_worked)
        return self.get_salary()


class Manager(FullTimeEmployee):
    def __init__(self, emp_id, name, department, monthly_salary, bonus):
        super().__init__(emp_id, name, department, monthly_salary)
        self.bonus = bonus

    def calculate_salary(self):
        """Polymorphism - overriding base method."""
        self.set_salary(self.monthly_salary + self.bonus)
        return self.get_salary()


def save_to_csv(employees, filename="payroll_data.csv"):
    """Saves payroll records to a CSV file (Bonus feature)."""
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Emp ID", "Name", "Department", "Type", "Salary"])
        
        for emp in employees:
            writer.writerow([
                emp.emp_id, 
                emp.name, 
                emp.department, 
                emp.__class__.__name__, 
                emp.calculate_salary()
            ])
    print(f"\n[INFO] Data successfully saved to {filename}")


def main():
    employees = []
    
    while True:
        print("\n" + "="*30)
        print("   Payroll Management System   ")
        print("="*30)
        print("1. Full-Time Employee")
        print("2. Intern")
        print("3. Contractor")
        print("4. Manager")
        print("5. View Payroll")
        print("6. Save Data to CSV")
        print("7. Exit")
        
        try:
            choice = int(input("\nEnter your choice (1-7): "))
        except ValueError:
            print("[ERROR] Invalid input! Please enter a number.")
            continue
            
        if choice in [1, 2, 3, 4]:
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            dept = input("Enter Department: ")
            
            try:
                if choice == 1:
                    monthly_salary = float(input("Enter Monthly Salary: "))
                    emp = FullTimeEmployee(emp_id, name, dept, monthly_salary)
                elif choice == 2:
                    stipend = float(input("Enter Stipend Amount: "))
                    emp = Intern(emp_id, name, dept, stipend)
                elif choice == 3:
                    hourly_rate = float(input("Enter Hourly Rate: "))
                    hours_worked = float(input("Enter Hours Worked: "))
                    emp = Contractor(emp_id, name, dept, hourly_rate, hours_worked)
                elif choice == 4:
                    monthly_salary = float(input("Enter Monthly Salary: "))
                    bonus = float(input("Enter Bonus: "))
                    emp = Manager(emp_id, name, dept, monthly_salary, bonus)
                    
                employees.append(emp)
                print(f"\n[SUCCESS] Employee '{emp.name}' added successfully!")
            except ValueError:
                print("\n[ERROR] Invalid numeric input! Please try again.")
                
        elif choice == 5:
            if not employees:
                print("\n[INFO] No employees found. Please add some first.")
            else:
                print("\n" + "-"*40)
                print("           Payroll Details           ")
                print("-"*40)
                total_payroll = 0
                for emp in employees:
                    salary = emp.calculate_salary()
                    total_payroll += salary
                    print(f"{emp} | Salary: ${salary:.2f}")
                print("-" * 40)
                print(f"Total Payroll to Disburse: ${total_payroll:.2f}")
                print("-" * 40)
                
        elif choice == 6:
            if not employees:
                print("\n[INFO] No employees to save.")
            else:
                save_to_csv(employees)
                
        elif choice == 7:
            print("\nExiting the Payroll Management System. Goodbye!")
            break
        else:
            print("\n[ERROR] Invalid choice! Please select an option between 1 and 7.")

if __name__ == "__main__":
    main()
