import json

class BaseResponse:
    def __init__(self):
        self.success = False
        self.error_code = 0
        self.error_msg = ''
        self.result = ''

    def to_json(self):
        return json.dumps(self.__dict__)

class SuccessResponse(BaseResponse):

    def __init__(self, result):
        super().__init__()
        self.success = True
        if isinstance(result, (dict, list, tuple, str, int, float, bool)):
            self.result = result
        else:
            self.result = result.__dict__


class FailResponse(BaseResponse):
    def __init__(self, error_code, error_msg):
        super().__init__()
        self.error_code = error_code
        self.error_msg = 'lanthar error ' + str(error_msg)



