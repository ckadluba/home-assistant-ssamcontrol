import test_parameters

# Create test_parameters.py with content like this:
# parameters = {
#     "account": <account name>,
#     "password": <password>,
#     "pin_code": <4-digit pin code>,
#     "mode": "disarm"
# }

class log:
    def info(message, *args):
        print(message, *args)
    def error(message, *args):
        print(message, *args)

class task:
    def executor(func, *args, **kwargs):
        return func(*args, **kwargs)

def service(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

exec(open('./ssamcontrol.py').read())

ssamcontrol(**test_parameters.parameters)
