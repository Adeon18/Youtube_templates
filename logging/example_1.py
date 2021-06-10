"""
Example 1 of logging usage
"""
import logging

logging.basicConfig(filename="logs.log", filemode="w", level=logging.DEBUG)

def process1():
    """
    Process 1, okay?
    """
    logging.info("Process 1 is complete...")
    return

def process2():
    """
    Process 2, okay?
    """
    logging.info("Process 2 is complete...")
    return

def process3():
    """
    Process 3, okay?
    """
    logging.info("Process 3 is complete...")
    return

logging.info("Started program execution")
while True:
    try:
        process = input("Choose the process you want to complete: ")
        if process == "1":
            logging.info("User chose process 1")
            process1()
        elif process == "2":
            logging.info("User chose process 2")
            process2()
        elif process == "3":
            logging.info("User chose process 3")
            process3()
        else:
            logging.warning(f"User chose a process that is not in the list of processes. Input is {process}")
    except KeyboardInterrupt:
        logging.info("User has exited the program")
        break

logging.info("Finished the program execution")