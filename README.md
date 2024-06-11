This script validates an email address entered by the user based on a specified regular expression pattern. It checks if the email address matches the given conditions and prints whether the email is valid or invalid.

Requirements
Python 3.x
Usage
Clone the repository or download the script file.
Run the script using Python.
Enter an email address when prompted.
Script Details
The script performs the following steps:

Imports the re module for regular expression operations.
Defines a regular expression pattern email_conditions to specify the conditions an email address must meet to be considered valid.
Prompts the user to enter an email address.
Checks if the entered email address matches the pattern using re.search.
Prints "Valid email" if the email address matches the pattern, otherwise prints "Invalid email".

This pattern checks for the following conditions:

The email address must start with one or more lowercase letters (^[a-z]+).
It may optionally contain a dot, underscore, or slash followed by one or more lowercase letters or digits ([/._]?[a-z 0-9]+).
It must contain an "@" symbol ([@]).
This is followed by one or more word characters (/w+).
It must contain a dot ([.]).
It ends with two or three word characters (/w{2,3}$).
Notes
The current regular expression pattern may not cover all valid email formats according to the standard email format specifications (RFC 5322). For more comprehensive email validation, consider using more advanced libraries or patterns.
The script currently only accepts lowercase letters at the beginning of the email address and certain special characters. Adjust the regular expression pattern as needed for your specific requirements.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request for improvements or bug fixes.
