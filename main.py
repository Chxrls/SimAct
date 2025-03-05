def calculate_sss(): #sss
    return 1200

def calculate_philhealth(salary): #philhealth
    return (salary * 0.05) / 2

def calculate_pagibig(): #pag-ibig
    return 100

def calculate_tax(): #tax
    return 1875

def compute_deductions(salary): #salary computations
    sss = calculate_sss()
    philhealth = calculate_philhealth(salary)
    pagibig = calculate_pagibig()
    tax = calculate_tax()

    deductions = sss + philhealth + pagibig + tax
    net_salary = salary - deductions

    return sss, philhealth, pagibig, tax, deductions, net_salary

def main():
    salary = float(input("Enter your monthly salary: "))
    
    sss, philhealth, pagibig, tax, deductions, net_salary = compute_deductions(salary)
    
    print("Gross Salary:", salary)
    print("SSS Deduction:", sss)
    print("PhilHealth Deduction:", philhealth)
    print("Pag-IBIG Deduction:", pagibig)
    print("Tax Deduction:", tax)
    print("Total Deductions:", deductions)
    print("Net Salary:", net_salary)

main()
