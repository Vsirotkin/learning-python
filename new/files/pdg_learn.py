# learn how to work with python debugger
import pdb


def debug(a, b) -> object:
    return print(a + b)

pdb.set_trace()
debug(2, 'seven')
