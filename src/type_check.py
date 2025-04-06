
class TypeCheckError(TypeError):
    pass

def type_check(correct_type):
    """
    checks if the type is correct
    """
    def decorator(func):
        def check_args(args):
            if isinstance(args , correct_type):
                return func(args)
            else:
                raise TypeCheckError("This is not the right type!")
        return check_args
    return decorator



@type_check(int)
def times2num(num):
    return num*2

if __name__ == '__main__':
    print(times2num(6))