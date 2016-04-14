from ctypes import cdll,c_int
from ctypes.util import find_library
import os
import time
import math
import sys



def show_cpython_vs_binary(cpython_time,binary_time,latency_time=0):
    print("Binary time : "+str(binary_time))
    if latency_time != 0:
        print("Latency time (settings up binary): "+str(latency_time))
    print("CPython time : "+str(cpython_time))

    if (binary_time + latency_time) < cpython_time:
        print("Speed increase with binary+latency : x"+str(cpython_time/(binary_time+latency_time)))
    elif (binary_time > cpython_time) and latency_time != 0:
        print("Binary never worth, cpython faster: x"+str(binary_time/cpython_time))
    elif (binary_time > cpython_time) and latency_time == 0:
        print("Cpython faster: x"+str(binary_time/cpython_time))
    else:
        print("Loop for being worth the price : "+str(math.ceil(latency_time/(cpython_time-binary_time))))


if __name__ ==  "__main__" :
    # Save local path in SRC (taking care of utf-8 possibility for python2.7)
    if sys.version_info < (3,0):
        SRC = os.path.dirname(os.path.abspath(__file__)).decode("utf-8")
    else:
        SRC = os.path.dirname(os.path.abspath(__file__))

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
    binary_time = end_binary_code-start_binary_code
    cpython_time = end_cpython_code-start_cpython_code
    latency_time = end_latency-start_latency - binary_time
    print("Binary time : "+str(binary_time))
    print("Latency time (settings up binary): "+str(latency_time))
    print("CPython time : "+str(cpython_time))

    if (binary_time + latency_time) < cpython_time:
        print("Speed increase with binary+latency : x"+str(cpython_time/(binary_time+latency_time)))
    elif (binary_time > cpython_time):
        print("Binary never worth, cpython faster: x"+str(binary_time/cpython_time))
    else:
        print("Loop for being worth the price : "+str(math.ceil(latency_time/(cpython_time-binary_time))))
