SSS_DEDUCTION = 1200
PHILHEALTH_RATE = 0.05
PAGIBIG_CONTRIBUTION = 100
INCOME_TAX = 1875

def calculate_sss_deduction():
    """Calculate the SSS (Social Security System) deduction, which is a fixed amount."""
    return SSS_DEDUCTION

def calculate_philhealth_contribution(salary):
    """Calculate the PhilHealth contribution based on the salary."""
    return (salary * PHILHEALTH_RATE) / 2

def calculate_pagibig_contribution():
    """Calculate the Pag-IBIG contribution, which is a fixed amount."""
    return PAGIBIG_CONTRIBUTION

def calculate_income_tax():
    """Calculate the income tax, which is a fixed amount."""
    return INCOME_TAX

def calculate_deductions(salary):
    """Calculate all deductions and net salary based on the provided salary."""
    sss = calculate_sss_deduction()
    philhealth = calculate_philhealth_contribution(salary)
    pagibig = calculate_pagibig_contribution()
    tax = calculate_income_tax()

    deductions = sss + philhealth + pagibig + tax
    net_salary = salary - deductions

    return sss, philhealth, pagibig, tax, deductions, net_salary


def main():
    """Main function to handle user input and display salary details."""
    while(True):
        try:
            salary = float(input("Enter your monthly salary: "))
            if salary <= 0:
                print("Invalid input. Salary must be greater than zero.")
                continue
            break
        except:
            print("Invalid input. Please enter a valid number.")

    sss, philhealth, pagibig, tax, deductions, net_salary = calculate_deductions(salary)

    print(f"\nGross Salary: ₱{salary:,.2f}")
    print(f"SSS Deduction: ₱{sss:,.2f}")
    print(f"PhilHealth Deduction: ₱{philhealth:,.2f}")
    print(f"Pag-IBIG Deduction: ₱{pagibig:,.2f}")
    print(f"Tax Deduction: ₱{tax:,.2f}")
    print(f"Total Deductions: ₱{deductions:,.2f}")
    print(f"Net Salary: ₱{net_salary:,.2f}")

main()