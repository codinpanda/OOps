# OOP Mini Project Lab — Payroll Management System

## Objective
The objective of this project is to build a Payroll Management System using Python OOP concepts including Classes, Objects, Encapsulation, Inheritance, and Polymorphism.

## Features
- Interactive Command Line Interface (CLI)
- Dynamically add different types of employees (Full-Time, Intern, Contractor, Manager).
- Calculate and view individual salaries as well as total payroll.
- Handle invalid inputs seamlessly.
- **Bonus Feature:** Included a Department attribute for employees.
- **Bonus Feature:** Save payroll data to a CSV file (`payroll_data.csv`).
- **Bonus Feature:** Included a `Manager` class that inherits from `FullTimeEmployee` with an added bonus attribute.

## Object-Oriented Programming (OOP) Concepts Used

### 1. Classes and Objects
- Defined several classes: `Employee`, `FullTimeEmployee`, `Intern`, `Contractor`, and `Manager`.
- Objects (instances) of these classes are created dynamically when the user inputs employee details through the CLI.

### 2. Encapsulation
- The `__salary` attribute in the base `Employee` class is made private to prevent direct access or modification from outside the class.
- Getter (`get_salary()`) and setter (`set_salary()`) methods are implemented to securely access and update the private salary attribute.

### 3. Inheritance
- Reusability is achieved through inheritance.
- `FullTimeEmployee`, `Intern`, and `Contractor` inherit common attributes (`emp_id`, `name`, `department`) and methods from the base `Employee` class.
- The `Manager` class inherits from `FullTimeEmployee` (Multi-level inheritance), reusing the `monthly_salary` logic while adding a specific `bonus` attribute.

### 4. Polymorphism
- The `calculate_salary()` method is defined in the base `Employee` class and overridden in each derived class (`FullTimeEmployee`, `Intern`, `Contractor`, `Manager`).
- When `emp.calculate_salary()` is called in a loop over a list of mixed employee objects, Python dynamically invokes the correct implementation depending on the specific object type.

## How to Run
1. Ensure you have Python installed on your system.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using the command: `python main.py`
5. Follow the interactive menu prompts to add employees and manage payroll.
