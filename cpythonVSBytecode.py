from ctypes import cdll,c_int
from ctypes.util import find_library
import os
import time

# Save local path in SRC (taking care of utf-8 possibility)
SRC = os.path.dirname(os.path.abspath(__file__)).decode("utf-8")
# Size of our list and array
N = 100000


# Create a list with n element. Un = n
# [0,1,2,3,4,...,999]
my_int_list = [i for i in range(N)]

# Measure setting up time for binary code
start_latency = time.time()

# Load our library from local path
loaded_lib = cdll.LoadLibrary(SRC+"/my_library.so")

# We want to execute add_one function
# from our library
add_one_loop = loaded_lib.add_one



# We create a array ctype class which can handle
# our list in size (int * size_list)
Array_class = (c_int * len(my_int_list))

# We create an instance of our class
# and we put our list in it
my_int_array = Array_class(*my_int_list)

#Set the binary function args types.
# 1. pointer of our array
# 2. size of our array
add_one_loop.argtypes= [Array_class,c_int]

# Execute binary code (we measure time too)
start_binary_code = time.time()
add_one_loop(my_int_array, len(my_int_list))
end_binary_code = time.time()

# We store result back in our python list
my_int_list = [my_int_array[i] for i in range(len(my_int_list))]

end_latency = time.time()



#Now we can compare speed with python bytecode
start_cpython_code = time.time()
for i in range(len(my_int_list)):
    my_int_list[i]+= 1
end_cpython_code = time.time()

# We modified 2 times so Un = n+2
# [2,3,4,5,...,1001]
assert(my_int_list[0] == 2)
assert(my_int_list[len(my_int_list)-1] == (len(my_int_list)-1)+2)

#Time to compare time !
print "Binary time : "+str(end_binary_code-start_binary_code)
print "Binary time with settings up (latency) : "+str(end_latency-start_latency)
print "CPython time : "+str(end_cpython_code-start_cpython_code)
