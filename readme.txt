HARBORFLOW DISPATCH CONSOLE - TEAM README

Run instructions
----------------
Command:
Python version tested:

Team members and concrete contributions
---------------------------------------
Name: Hannes Lindberg
Contribution:
- Task 1
- Task 6

Name: Hugo Karlsson
Contribution:
- Task 2
- Task 4
- Task 5

Name: Brian Rauch
Contribution: 
- Task 3
- Task 7

Nam: Aytunch Tuzdzhu
Contribution:
- Task 8
- Task 9

Design notes
------------
- Used clear() function to make the UI clean. 
- Also used if statement to make clear() function cross-platform for windows, mac and linux

Main function boundaries:

How input validation is organized:
- Used while loop for easy validations and try-except loop for complex validations
- Put validation loop inside the cases so after every invalid input, just the effected part will be repeat.

How shared calculations are reused:
- Created a calculation function called "calculate_delivery_quote".
- Reused it to calculate the quote variable in Task 3.
- Reused it to calculate the standard, express, and priority variables in Task 9.

Known limitations
-----------------
There are no Limitations.

What we have done on Task 8:
- added try-except loop for service selecting part (Line 45-51)
- added while loop in Case 3 (Line 42-58)
- added while and try-except loop in Case 5 (Line 61-84)
- added while loop in case 6 (Line 84-104)
- added while loop in case 7 (Line 104-124)
- added while loop in case 8 (Line 200-219)