class Employee:
    def __init__(self, emp_id, name, salary, department):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.department = department

    def display_details(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Salary: ${self.salary}, Department: {self.department}")

class Developer(Employee):
    def __init__(self, emp_id, name, salary, department, programming_language, experience):
        super().__init__(emp_id, name, salary, department)
        self.programming_language = programming_language
        self.experience = experience

    def display_details(self):
        super().display_details()
        print(f"Language: {self.programming_language}, Experience: {self.experience} years")

if __name__ == "__main__":
    emp1 = Employee(101, "Alice Smith", 60000, "HR")
    dev1 = Developer(102, "Bob Johnson", 95000, "Engineering", "Python", 5)
    dev2 = Developer(103, "Charlie Brown", 85000, "Engineering", "Java", 3)
    
    print("Employee Details:")
    emp1.display_details()
    print("-" * 20)
    
    print("Developer 1 Details:")
    dev1.display_details()
    print("-" * 20)
    
    print("Developer 2 Details:")
    dev2.display_details()
