# Define the Employee class
class Employee:
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_pay(self):
        if self.hours_worked > 40:
            overtime_hours = self.hours_worked - 40
            overtime_pay = overtime_hours * self.hourly_rate * 1.5
            regular_pay = 40 * self.hourly_rate
            return regular_pay + overtime_pay
        else:
            return self.hours_worked * self.hourly_rate

# Define the Manager subclass
class Manager(Employee):
    def __init__(self, name, hours_worked, hourly_rate, bonus):
        super().__init__(name, hours_worked, hourly_rate)
        self.bonus = bonus

    def calculate_pay(self):
        base_pay = super().calculate_pay()
        return base_pay + self.bonus

# Create instances for Employee and Manager
employee = Employee("John Doe", 45, 20)
manager = Manager("Jane Smith", 50, 30, 1000)

# Calculate and print the total pay for both
print(f"Total pay for {employee.name}: ${employee.calculate_pay()}")
print(f"Total pay for {manager.name}: ${manager.calculate_pay()}")
