import sys
import logging

def error_message_detail(error):
    """
    Create a detailed error message with filename, line number, and error text.
    """
    _, _, exc_tb = sys.exc_info()  # Get exception traceback
    file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown File"
    line_number = exc_tb.tb_lineno if exc_tb else "Unknown Line"
    error_message = f"Error in file: {file_name}, line: {line_number}, message: {str(error)}"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message)

    def __str__(self):
        return self.error_message
