from typing import List

def base_response(code, msg, data = None):
    if data is None:
        data = []
    result = dict(code=code, message=msg, data=data)
    return result


def err_response(code=-1, msg='failed', data=None):
    return base_response(code, msg, data)


def ok_response(data=None, msg=''):
    return base_response(200, msg, data)



