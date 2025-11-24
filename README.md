# Shopkeeper Profit Calculator

*Name:* Atharv Bisht  
*Reg No:* 25BCE10596  
*Course:* CSE1021 – Introduction to Problem Solving and Programming

This is a small Python project that helps a shopkeeper find whether a product gives profit, loss or neither.  
The program also stores every calculation in a CSV file and lets the user view or clear the history whenever needed.

## Overview
The project takes the Cost Price (CP) and Selling Price (SP) as input from the user and calculates:
- Profit or Loss
- The amount
- The percentage  

The program is menu-driven and divided into multiple modules to keep the code simple and easy to understand.  
All previous calculations are saved into a CSV file so the user can check them later.

## Features
- Calculate Profit / Loss
- Shows percentage gained or lost
- Saves every record automatically
- View history anytime
- Clear complete history
- Menu-based interface
- Uses 5 easy modules

## Technologies Used
- *Python 3*
- Built-in modules:  
  - `csv`
  - `os.path`

## Steps to Install and Run the Program

1. Download this project or clone the repository to your computer.  
2. Make sure all the Python files (main.py, product.py, calculator.py, history.py, menu.py) are in the same folder.  
3. Open a terminal or command prompt in that project folder.  
4. Make sure Python 3 is installed on your system.  
5. Run the program using:
   python main.py
6. The menu will appear on the screen. Choose any option by typing the number:
   - *1* → Calculate Profit/Loss  
   - *2* → View saved history  
   - *3* → Clear the history  
   - *4* → Exit the program

## Project Modules and Their Functions

### *1. main.py*
- Controls the whole program  
- Accepts user choice  
- Calls other modules  
- Shows final result  

### *2. product.py*
- Asks the user to enter CP and SP  
- Returns them to the main program  

### *3. calculator.py*
- Checks if the user made Profit / Loss / None  
- Calculates amount and percentage  
- Sends the results back to main.py

### *4. history.py*
- Creates the CSV file if it doesn't exist  
- Saves each record  
- Shows full history in a list format  
- Clears the history when needed  

### *5. menu.py*
- Displays the menu options  
- Makes the interface cleaner and more readable  

## Conclusion
The project is simple, modular, and easy to use.  
It demonstrates the use of basic Python concepts like functions, file handling, and modular programming.
