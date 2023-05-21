import os
import sys
from Src.logger import logging

class CustomException(Exception):

    def __init__(self, error_message:Exception, error_detail:sys):
        super().__init__(error_message)
        self.error_message= CustomException.error_message_detail(error_message, error_detail=error_detail)

    @staticmethod
    def error_message_detail(error:Exception, error_detail:sys)->str:
        _, _, exc_tb =error_detail.exc_info()
        line_number=exc_tb.tb_frame.f_lineno

        # Extracting file name from exception traceback
        file_name=exc_tb.tb_frame.f_code.co_filename

        # Preparing message
        error_message= f"Error Occured python script name[{file_name}]" \
                       f' line Number[{exc_tb.tb_lineno}] error message [{error}].'

        return error_message
    
    def __str__(self):
        return self.error_message
    
    def __repr__(self):
        return CustomException.__name__.__str__()
    
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Division by Zero is not Possible")
        raise CustomException(e,sys)
