"""
1. Import C++ modules so they can be called as functions
"""
import ctypes

# Load the C++ library
lib = ctypes.cdll.LoadLibrary('./lib/libpy_ctypes_example.so')

# Define the argument and return types of the functions
lib.add_int.argtypes = [ctypes.c_int, ctypes.c_int]
lib.add_int.restype = ctypes.c_int

lib.add_double.argtypes = [ctypes.c_double, ctypes.c_double]
lib.add_double.restype = ctypes.c_double

lib.add_float.argtypes = [ctypes.c_float, ctypes.c_float]
lib.add_float.restype = ctypes.c_float

lib.add_char.argtypes = [ctypes.c_char, ctypes.c_char]
lib.add_char.restype = ctypes.c_char

lib.add_string.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
lib.add_string.restype = ctypes.c_char_p

"""
2. Define the Python functions that call the C++ functions
"""
def add_int(a, b):
    return lib.add_int(a, b)

def add_double(a, b):
    return lib.add_double(a, b)

def add_float(a, b):
    return lib.add_float(a, b)

def add_char(a, b):
    return lib.add_char(a, b)

def add_string(a, b):
    return lib.add_string(a, b)

"""
3. Test the functions
"""
print(add_int(1, 2))
print(add_double(1.0, 2.0))
print(add_float(1.0, 2.0))
print(add_char('a', 'b'))
print(add_string("hello", "world"))