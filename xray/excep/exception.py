import os 
import sys 
def error_message_detail(error: Exception,error_detail:sys) -> str:
    _,_,exc_tb=error_detail.exc_info()

    file_name:str=os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    error_message:str ="Error occured in[{0}] line [{1}] message[2]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )

    return error_message

class xrayexception(Exception):
    def __init__(self,error_message,error_detail):
        super().__init__(error_message)
        self.error_message:str =error_message_detail(
            error_message,error_detail=error_detail
        )

    def __str__(self):
        return self.error_message
