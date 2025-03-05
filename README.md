# Technical Debt Management Activity

## Overview

This project is a Salary Deduction Calculator that computes various deductions from an employee's salary, such as SSS, PhilHealth, Pag-IBIG, and income tax. The refactored version improves code readability, modularity, and maintainability while addressing technical debt issues.

## Refactoring Changes

### As for our role the Refactoring Specialists(Antinero,Tarre) we focused on improving code readability through better naming conventions and formatting. The key refactoring improvements include:

1. Renamed functions and variables to be more descriptive and consistent.

2. Ensured that each calculation was handled in separate, reusable functions.

3. Constants were defined for better maintainability.

4. Implemented input validation to handle invalid salary inputs.

5. Improved print statements for better readability.

## Technical Debt Identified

### Before refactoring, the code had the following issues:

1. Some function names were unclear or inconsistent.

2. Some calculations were embedded directly in the main logic instead of separate functions.

3. Deduction amounts and tax rates were hardcoded, making updates difficult.

4. The program did not properly handle invalid user inputs.

5. Certain calculations lacked proper reuse, making the code less efficient.
   

## Challenges Faced & Solutions

Implemented a while loop with try-except to ensure only valid numerical input is accepted.

Maintained clarity in function naming while keeping computations simple.

Used Python's built-in string formatting for a clean and professional display of salary details.




## The code consists of the procedural program to solve salary deductions without using object-oriented programming (OOP) concepts like classes or objects. (Cagampang & Colegado)

1. Technical Debt Identified
   
Hard-Coded Constants: Constants like SSS_DEDUCTION, PHILHEALTH_RATE, PAGIBIG_CONTRIBUTION, and INCOME_TAX are hardcoded in the script. 

This creates a lack of flexibility for changes and maintenance, as modifications would require changes directly in the code rather than external configuration.

Duplication: The logic for calculating different deductions (SSS, PhilHealth, Pag-IBIG, and tax) is somewhat redundant, making the code harder to extend in the future.

No Modularity: Functions are somewhat scattered, and there is room for improving their clarity and structure.


2. Refactoring Improvements Made
   
Parameterization:Refactored the functions to allow for a more dynamic approach.

**For example, the calculate_philhealth_contribution could use a parameterized rate, and calculate_income_tax could be adjusted to accept varying rates based on the salary brackets.**

Consolidation of Constants: Moved constants like SSS_DEDUCTION, PHILHEALTH_RATE, etc., into a configuration or constants section to make it easier to modify.

Improved Functionality: The calculate_deductions function could be enhanced by adding more deductions or tax brackets in the future without modifying the core logic.

Validation Improvement: The main function’s input validation ensures that users only enter positive numbers, improving the program's robustness.


3. Challenges Faced & Solutions
   
(A)Challenge: Handling salary deductions based on varied input (like salary changes or new laws affecting contributions) was tricky, as the existing hardcoded deductions limit flexibility.

**Solution: By refactoring the code to accept dynamic parameters, the program can now adjust more easily to future changes.**

(B)Challenge: Input validation and handling edge cases such as non-numeric input or negative salaries.

**Solution: Improved error handling and user feedback were added to ensure the program doesn't crash when given invalid inputs.**

(C)Challenge: The readability and maintainability of the code could be better, especially if the logic for deductions needs expansion.

**Solution: Better structure was applied by grouping related deduction functions, improving the overall readability and making the code easier to extend.**
