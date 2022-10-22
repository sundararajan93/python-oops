class Vehicle:

    def __init__(self, color, license_plate, is_electric):
        self.color = color
        self.license_plate = license_plate
        self.is_electric = is_electric

    def show_license(self):
        print(self.license_plate)

    def show_info(self):
        print("Vehicle Info:")
        print(f"Color - {self.color}")
        print(f"License Plate - {self.license_plate}")
        print(f"Is Electric - {self.is_electric}")

class Employee:

    def __init__(self, name, employee_no, vehicle):
        self.name = name
        self.employee_no = employee_no
        self.vehicle = vehicle

    def show_employee(self):
        print("Employee Info:")
        print(f"Name - {self.name}")
        print(f"Employee No - {self.employee_no}")

    def show_vehicle_info(self):
        self.vehicle.show_info()


employee_vehicle = Vehicle("Blue", "TN 19 V 0531", is_electric=False)
employee = Employee("Sundar", 113453, employee_vehicle)

print(employee.name)
print(employee.employee_no)

print("___________________")

employee.show_employee()
employee.show_vehicle_info()

print("___________________")

print(employee.vehicle.color)
print(employee.vehicle.license_plate)
print(employee.vehicle.is_electric)
