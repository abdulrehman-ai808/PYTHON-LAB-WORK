import csv

try:
    n = int(input("Enter number of employees: "))

    with open("payroll.csv", "w", newline="") as file:

        writer = csv.writer(file)

        # Write header
        writer.writerow([
            "ID",
            "Name",
            "Basic",
            "Allowance",
            "Deduction",
            "Net Salary"
        ])

        # Enter employee details
        for i in range(n):

            print("\nEnter Employee Details")

            emp_id = input("Employee ID: ")
            name = input("Employee Name: ")

            basic = float(input("Basic Salary: "))
            allowance = float(input("Allowance: "))
            deduction = float(input("Deduction: "))

            # Calculate net salary
            net_salary = basic + allowance - deduction

            # Write employee record
            writer.writerow([
                emp_id,
                name,
                basic,
                allowance,
                deduction,
                net_salary
            ])

    print("\nPayroll data saved successfully to payroll.csv")

except ValueError:
    print("Invalid input. Please enter numeric values correctly.")

except Exception as e:
    print(f"Error: {e}")