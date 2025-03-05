# Constants for deductions
SSS_DEDUCTION = 1200
PAGIBIG_DEDUCTION = 100

def calculate_sss():
    """Calculate SSS deduction."""
    return SSS_DEDUCTION

def calculate_philhealth(salary):
    """Calculate PhilHealth deduction (5% of salary, shared equally)."""
    return (salary * 0.05) / 2

def calculate_pagibig():
    """Calculate Pag-IBIG deduction."""
    return PAGIBIG_DEDUCTION

def calculate_tax(salary):
    """Calculate tax based on salary brackets."""
    if salary <= 20833:
        return 0
    elif salary <= 33333:
        return (salary - 20833) * 0.20
    elif salary <= 66667:
        return 2500 + (salary - 33333) * 0.25
    elif salary <= 166667:
        return 10833 + (salary - 66667) * 0.30
    else:
        return 40833.33 + (salary - 166667) * 0.35

def compute_deductions(salary):
    """Compute all deductions and net salary."""
    sss = calculate_sss()
    philhealth = calculate_philhealth(salary)
    pagibig = calculate_pagibig()
    tax = calculate_tax(salary)

    deductions = sss + philhealth + pagibig + tax
    net_salary = salary - deductions

    return sss, philhealth, pagibig, tax, deductions, net_salary

def get_valid_salary():
    """Get a valid salary input from the user."""
    while True:
        try:
            salary = float(input("Enter your monthly salary: "))
            if salary >= 0:
                return salary
            else:
                print("Salary must be a positive number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    """Main function to run the program."""
    salary = get_valid_salary()
    
    sss, philhealth, pagibig, tax, deductions, net_salary = compute_deductions(salary)
    
    print("\nGross Salary:", salary)
    print("SSS Deduction:", sss)
    print("PhilHealth Deduction:", philhealth)
    print("Pag-IBIG Deduction:", pagibig)
    print("Tax Deduction:", tax)
    print("Total Deductions:", deductions)
    print("Net Salary:", net_salary)

# Run the program
main()