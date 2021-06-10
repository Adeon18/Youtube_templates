"""
Example 2 of logging usage
"""
import logging

logging.basicConfig(filename="logs.log", filemode="w", level=logging.DEBUG)

logging.info("Started program execution")

first_num = input("Enter the first number: ")

operator = input("Enter the operation: ")

second_num = input("Enter the second number: ")

try:
    first_num = int(first_num)
    logging.debug("First number converted to int")
    second_num = int(second_num)
    logging.debug("Second number converted to int")
except ValueError:
    logging.exception("Cannot perform the operation because one of the variables is not a number")


if operator not in ['-', '+']:
    logging.error(f"The calculator does not support an operator {operator}")
else:
    logging.info("Starting the operation...")
    if operator == "+":
        print(first_num + second_num)
        logging.debug("Addition was performed")
    elif operator == "-":
        print(first_num - second_num)
        logging.debug("Substraction was performed")


logging.info("Program execution ended")